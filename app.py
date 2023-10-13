import geopandas as gpd
import matplotlib.pyplot as plt

# POLYGON PRINT AND COORDINATES 
print("Script starting...")

try:
    print("Loading shapefile...")
    gdf = gpd.read_file('CA_Counties/CA_Counties_TIGER2016.shp')

    print("Filtering data for Orange County...")
    orange_county = gdf[gdf['NAME'] == 'Orange']

    print("Extracting coordinates...")
    if not orange_county.empty:
        polygon = orange_county.geometry.iloc[0]
        exterior_coords = list(polygon.exterior.coords)
        
        # Formatting coordinates as [longitude, latitude]
        formatted_coords = [[x, y] for x, y in exterior_coords]
        
        print("Coordinates of Orange County polygon:")
        for coord in formatted_coords:
            print(coord)
    else:
        print("No data found for Orange County.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

print("Script completed.")


# import geopandas as gpd
# import matplotlib.pyplot as plt


# def save_coords_to_file(coords, filename):
#     with open(filename, 'w') as file:
#         for coord in coords:
#                file.write(f"{coord[1]}, {coord[0]}\n")

# print("Script starting...")

# try:
#     print("Loading shapefile...")
#     gdf = gpd.read_file('CA_Counties/CA_Counties_TIGER2016.shp')

#     print("Filtering data for Orange County...")
#     orange_county = gdf[gdf['NAME'] == 'Orange']

#     print("Extracting coordinates...")
#     if not orange_county.empty:
#         polygon = orange_county.geometry.iloc[0]
#         exterior_coords = list(polygon.exterior.coords)
        
#         # Reducing precision and subsampling every 10th coordinate
#         formatted_coords = [[round(x, 2), round(y, 2)] for i, (x, y) in enumerate(exterior_coords) if i % 10 == 0]
        
#         print(f"Saving {len(formatted_coords)} coordinates to file...")
#         save_coords_to_file(formatted_coords, 'orange_county_coords.txt')
#     else:
#         print("No data found for Orange County.")
# except Exception as e:
#     print(f"An error occurred: {str(e)}")

# print("Script completed.")

