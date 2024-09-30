import requests
from bs4 import BeautifulSoup

def display_ascii_art():
    print("\033[94m" + """
         ooo
        / : \\
       / o0o \\
 _____"~~~~~~~"_____
 \\+###|U * * U|###+/
  \\...!(.>..<)!.../
   ^^^^o|   |o^^^^
+=====}:^^^^^:{=====+#
.____  .|!!!|.  ____.
|#####:/" " "\\:#####|
|#####=|  O  |=#####|
|#####>\\_____/<#####|
 ^^^^^   | |   ^^^^^
         o o
    """ + "\033[0m")

def scrape_orbit_info(norad_id):
    orbit_url = f"https://isstracker.pl/en/satelity/{norad_id}"
    orbit_response = requests.get(orbit_url)

    if orbit_response.status_code != 200:
        print("Failed to retrieve the orbit information.")
        return "Perigee not found", "Apogee not found", "Orbit Slope not found"

    orbit_soup = BeautifulSoup(orbit_response.content, 'html.parser')

    # Extracting Perigee
    perigee_row = orbit_soup.find('td', string="Perigee")
    perigee_info = perigee_row.find_next_sibling('td').text.strip() if perigee_row else "Perigee not found"

    # Extracting Apogee
    apogee_row = orbit_soup.find('td', string="Apogee")
    apogee_info = apogee_row.find_next_sibling('td').text.strip() if apogee_row else "Apogee not found"

    # Extracting Orbit slope (Inclination)
    orbit_slope_row = orbit_soup.find('td', string="Orbit slope (inclination)")
    orbit_slope_info = orbit_slope_row.find_next_sibling('td').text.strip() if orbit_slope_row else "Orbit Slope not found"

    return perigee_info, apogee_info, orbit_slope_info

def get_satellite_info(norad_id):
    url = f"https://www.satcat.com/sats/{norad_id}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve the page. Please check the NORAD ID or try again later.")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting satellite name
    sat_name_header = soup.find('h1', class_="Home_page-sat-header__evnV7")
    sat_name = sat_name_header.find('b').text if sat_name_header else "Satellite name not found"

    # Extracting mission
    mission = soup.find('td', string="Mission")
    mission_info = mission.find_next_sibling('td').text if mission else "Mission not found"

    # Extracting manufacturer
    manufacturer = soup.find('td', string="Manufacturer")
    manufacturer_info = manufacturer.find_next_sibling('td').text if manufacturer else "Manufacturer not found"

    # Extracting bus & motor
    bus_motor = soup.find('td', string="Bus & Motor")
    bus_motor_info = bus_motor.find_next_sibling('td').text if bus_motor else "Bus & Motor not found"

    # Extracting geo
    geo = soup.find('td', string="Orbit")
    geo_info = geo.find_next_sibling('td').find('span').text if geo else "GEO not found"

    # Extracting last TLE update
    last_tle_update = soup.find('td', string="Last TLE update")
    last_tle_update_info = last_tle_update.find_next_sibling('td').text if last_tle_update else "Last TLE update not found"

    # Extracting mass
    mass = soup.find('td', string="Mass")
    mass_info = mass.find_next_sibling('td').text if mass else "Mass not found"

    # Extracting launch date
    launch_date = soup.find('td', string="Launch date (UTC)")
    launch_date_info = launch_date.find_next_sibling('td').find('span').text if launch_date else "Launch date not found"

    # Extracting launch vehicle
    launch_vehicle = soup.find('td', string="Launch vehicle")
    launch_vehicle_info = launch_vehicle.find_next_sibling('td').find('span').text if launch_vehicle else "Launch vehicle not found"

    # Extracting launch site
    launch_site = soup.find('td', string="Launch site")
    launch_site_info = launch_site.find_next_sibling('td').find('span').text if launch_site else "Launch site not found"

    # Extracting object type
    object_type = soup.find('td', string="Object type")
    object_type_info = object_type.find_next_sibling('td').find('span').text if object_type else "Object type not found"

    # Extracting radar cross section
    radar_cross_section = soup.find('td', string="Radar Cross Section")
    radar_cross_section_info = radar_cross_section.find_next_sibling('td').text if radar_cross_section else "Radar Cross Section not found"

    # Extracting origin (modified)
    origin = soup.find('td', string="Origin")
    origin_info = origin.find_next_sibling('td').text.strip() if origin else "Origin not found"

    # Extracting Shape & HBR
    shape_hbr = soup.find('td', string="Shape & HBR")
    shape_hbr_info = shape_hbr.find_next_sibling('td').text if shape_hbr else "Shape & HBR not found"

    # Scraping orbit info from second source
    perigee_info, apogee_info, orbit_slope_info = scrape_orbit_info(norad_id)

    # Display satellite information
    print("\033[1m\033[97m" + f"\nSatellite Information for NORAD {norad_id}" + "\033[0m")
    print(f"Satellite Name: \033[94m{sat_name}\033[0m")
    print(f"Mission: \033[94m{mission_info}\033[0m")
    print(f"Manufacturer: \033[94m{manufacturer_info}\033[0m")
    print(f"Bus & Motor: \033[94m{bus_motor_info}\033[0m")
    print(f"Orbit: \033[94m{geo_info}\033[0m")
    print(f"Last TLE Update: \033[94m{last_tle_update_info}\033[0m")
    print(f"Mass: \033[94m{mass_info}\033[0m")
    print(f"Launch Date (UTC): \033[94m{launch_date_info}\033[0m")
    print(f"Launch Vehicle: \033[94m{launch_vehicle_info}\033[0m")
    print(f"Launch Site: \033[94m{launch_site_info}\033[0m")
    print(f"Object Type: \033[94m{object_type_info}\033[0m")
    print(f"Radar Cross Section: \033[94m{radar_cross_section_info}\033[0m")
    print(f"Origin: \033[94m{origin_info}\033[0m")
    print(f"Shape & HBR: \033[94m{shape_hbr_info}\033[0m")

    # Displaying orbit information from isstracker
    print(f"Perigee: \033[94m{perigee_info}\033[0m")
    print(f"Apogee: \033[94m{apogee_info}\033[0m")
    print(f"Orbit Slope (Inclination): \033[94m{orbit_slope_info}\033[0m")

if __name__ == "__main__":
    # Display ASCII art once at the top
    display_ascii_art()
    norad_id = input("\033[96mEnter NORAD ID: \033[0m")
    get_satellite_info(norad_id)
