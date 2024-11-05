import ee

# Initialize the Earth Engine API
ee.Initialize()

# Valencia center coordinates and buffer radius
VALENCIA_CENTER = ee.Geometry.Point([-0.3763, 39.4699])  # Longitude, Latitude of Valencia center
BUFFER_RADIUS = 200000  # 200 km radius

# Buffered geometry for Valencia
VALENCIA_COORDS = VALENCIA_CENTER.buffer(BUFFER_RADIUS)
