"""
Compute terrain effect over South America using tesseroids
"""
import time
from pathlib import Path
import boule as bl
import ensaio
import numpy as np
import pygmt
import verde as vd
import xarray as xr

import harmonica as hm

figs_dir = Path(__file__).parent / ".." / "figs"

fname = ensaio.fetch_earth_topography(version=1)
topo = xr.load_dataarray(fname)

region = (-85, -32, -58, 15)
topo = topo.sel(latitude=slice(*region[2:]), longitude=slice(*region[:2]))

ellipsoid = bl.WGS84

longitude, latitude = np.meshgrid(topo.longitude, topo.latitude)
reference = ellipsoid.geocentric_radius(latitude)
surface = topo + reference
density = xr.where(topo > 0, 2670.0, 1040.0 - 2670.0)

tesseroids = hm.tesseroid_layer(
    coordinates=(topo.longitude, topo.latitude),
    surface=surface,
    reference=reference,
    properties={"density": density},
)

# Create a regular grid of computation points located at 10km above reference
grid_longitude, grid_latitude = np.meshgrid(topo.longitude, topo.latitude)
grid_radii = ellipsoid.geocentric_radius(grid_latitude) + 10e3
grid_coords = (grid_longitude, grid_latitude, grid_radii)

# Compute gravity field of tesseroids
results_dir = Path(__file__).parent / ".." / "results"
outfile = results_dir / "terrain-effect.nc"
if outfile.exists():
    gravity = xr.load_dataset(outfile)
else:
    start = time.time()
    gravity = tesseroids.tesseroid_layer.gravity(
        grid_coords, field="g_z", disable_checks=True
    )
    end = time.time()
    print(f"Elapsed time: {end - start:.2f}s")

    gravity = vd.make_xarray_grid(
        grid_coords,
        gravity,
        data_names="g_z",
        dims=("latitude", "longitude"),
        extra_coords_names="radius",
    )
    gravity.to_netcdf(outfile)

# Plot gravity field
fig = pygmt.Figure()
maxabs = vd.maxabs(gravity.g_z)
pygmt.makecpt(cmap="polar", series=(-maxabs, maxabs))
fig.grdimage(
    gravity.g_z,
    projection="M15c",
    nan_transparent=True,
)
fig.basemap(frame=True)
fig.colorbar(frame='af+l"mGal"', position="JCR")
fig.coast(shorelines="0.5p,black", borders=["1/0.5p,black"])
fig.savefig(figs_dir / "terrain-correction-south-america.png")
fig.show()
