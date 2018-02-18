# We import our locations dictionary from data.py.
from data import locations

# We define a dictionary with our directions in. Each direction is a set of coordinates which, when added to a
# position, will move it in that direction. So for instance,
# if we are currently at (1, 1), moving east will result in (1+1, 1) = (2, 1).
# Moving west will result in (1-1, 1) = (0,1).
directions = {
    'west': (-1, 0),
    'east': (1, 0),
    'north': (0, -1),
    'south': (0, 1),
}

# This is our starting position.
position = (0, 0)

while True:
    # We find the actual name of our location by using the locations dictionary we imported from data.
    location = locations[position]
    print 'you are at the %s' % location

    valid_directions = {}
    # When iterating through a dictionary, it is often helpful to read both the keys(k) and values(v).
    for k, v in directions.iteritems():
        # For each direction, we calculate the new position (possible_position) if we were to take that direction.
        possible_position = (position[0] + v[0], position[1] + v[1])
        # We check to see if this position is in the list of locations.
        # get is a method on a dictionary which will return None if that key doesnt exist.
        possible_location = locations.get(possible_position)
        # If the possible location exists, we print it and add it to a dictionary which contains our valid directions.
        # We can use this later if the user decides to move there. It saves us doing all those calculations again.
        if possible_location:
            print 'to the %s is a %s' % (k, possible_location)
            valid_directions[k] = possible_position

    # We ask the user for a direction, and use the valid_directions dictionary to move us to that position.
    # When the loop begins again, we will be in that new position.
    direction = raw_input('which direction do you want to go?\n')

    new_position = valid_directions[direction]
    if new_position:
        position = new_position
    else:
        print "sorry, that isn't a valid direction"
