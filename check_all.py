#!/usr/bin/python3
from models import storage

# Dictionary of all classes and their modules
classes = {
    "BaseModel": "base_model",
    "User": "user",
    "State": "state",
    "City": "city",
    "Amenity": "amenity",
    "Place": "place",
    "Review": "review",
}

# Check if all classes are implemented and available
all_classes_available = True
for class_name, module_name in classes.items():
    try:
        exec(f"from models.{module_name} import {class_name}")
        print(f"{class_name} class is available.")
    except ImportError:
        print(f"{class_name} class is not available. Please implement it.")
        all_classes_available = False

# Test the available classes
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

# Create a new User
try:
    my_user = User()
    my_user.first_name = "Betty"
    my_user.last_name = "Bar"
    my_user.email = "airbnb@mail.com"
    my_user.password = "root"
    my_user.save()
    print(my_user)
except NameError:
    print("User class is not available.")

# Create a new State
try:
    my_state = State()
    my_state.name = "California"
    my_state.save()
    print(my_state)
except NameError:
    print("State class is not available.")

# Create a new City
try:
    my_city = City()
    my_city.state_id = my_state.id
    my_city.name = "San Francisco"
    my_city.save()
    print(my_city)
except NameError:
    print("City class is not available.")

# Create a new Amenity
try:
    my_amenity = Amenity()
    my_amenity.name = "Wi-Fi"
    my_amenity.save()
    print(my_amenity)
except NameError:
    print("Amenity class is not available.")

# Create a new Place
try:
    my_place = Place()
    my_place.city_id = my_city.id
    my_place.user_id = my_user.id
    my_place.name = "My house"
    my_place.description = "A beautiful house in San Francisco"
    my_place.number_rooms = 3
    my_place.number_bathrooms = 2
    my_place.max_guest = 5
    my_place.price_by_night = 200
    my_place.latitude = 37.7749
    my_place.longitude = -122.4194
    my_place.amenity_ids = [my_amenity.id]
    my_place.save()
    print(my_place)
except NameError:
    print("Place class is not available.")

# Create a new Review
try:
    my_review = Review()
    my_review.place_id = my_place.id
    my_review.user_id = my_user.id
    my_review.text = "Great place!"
    my_review.save()
    print(my_review)
except NameError:
    print("Review class is not available.")


def verify_relationships():
    """
    Verifies the relationships between different class instances.
    """
    all_objs = storage.all()

    for obj_id, obj in all_objs.items():
        class_name = obj.__class__.__name__

        if class_name == "City":
            # Verify that the state_id of the City instance exists
            state_id = obj.state_id
            if f"State.{state_id}" not in all_objs:
                print(f"City instance {obj_id} has an invalid state_id {state_id}")

        elif class_name == "Place":
            # Verify that the city_id and user_id of the Place instance exist
            city_id = obj.city_id
            user_id = obj.user_id
            if f"City.{city_id}" not in all_objs:
                print(f"Place instance {obj_id} has an invalid city_id {city_id}")
            if f"User.{user_id}" not in all_objs:
                print(f"Place instance {obj_id} has an invalid user_id {user_id}")

        elif class_name == "Review":
            # Verify that the place_id and user_id of the Review instance exist
            place_id = obj.place_id
            user_id = obj.user_id
            if f"Place.{place_id}" not in all_objs:
                print(f"Review instance {obj_id} has an invalid place_id {place_id}")
            if f"User.{user_id}" not in all_objs:
                print(f"Review instance {obj_id} has an invalid user_id {user_id}")


if all_classes_available:
    verify_relationships()
