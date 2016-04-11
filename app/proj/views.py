"""

"""
#todo Move out haversine

__author__ = 'donal'
__project__ = 'ribcage'

from flask import render_template, request, jsonify
from ..log_auth.views import login_confirmed, set_template
from . import proj
from math import radians, cos, sin, asin, sqrt
from config_vars import MAP_URL

# ME = (51.53, -0.14)
LALOS = [
    (54.3220, -5.7030),
    (50, -1),
    (52, 0.5),
    (52, -0.5)
]


def haversine((lat1, lon1), (lat2, lon2)):
    """
    Calculate the great circle distance between two points (km)
    on the earth (specified in decimal degrees).
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers.
    return round(c * r, 2)


# ========================
# SIMPLE STUFF
# ========================
@proj.route('/')
@proj.route('/home2')
def home2():
    return render_template('./proj/dummy.html')


@proj.route('/grid')
def grid():
    """
    return set_template('panelbuilder.html', lalos, '',
                        panel_args=dict(
                                patex='TITLE',
                                tadata='proj/grid_tdata.html',
                                wid=12
                        ))
    """
    return render_template('./proj/grid_tdata.html', map_url=MAP_URL)


@proj.route('/add_tees', methods=['POST', 'GET'])
def add_tees():
    # DATABASE: create an rV, and capture its id
    print request.args
    targ = (
        request.args.get('targLat', 0, type=float),
        request.args.get('targLong', 0, type=float)
    )
    rv_id = 1
    return render_template('./proj/add_tees.html', rv_id=rv_id, r_args=request.args.items(), targ=targ, map_url=MAP_URL)


# =================================================
# CALCULATION SCRIPTS
# USED FOR OUR AJAX REQUESTS
# =================================================
@proj.route('/_multilocs')
def multilocs():
    print 'multilocs'
    print request.args
    targ = (
        request.args.get('target[latitude]', 0, type=float),
        request.args.get('target[longitude]', 0, type=float)
    )
    me = {}
    me['latitude'] = request.args.get('lat', 0, type=float)
    me['longitude'] = request.args.get('long', 0, type=float)
    me['place'] = request.args.get('place', 'MISSING', type=str)

    _me = (me['latitude'], me['longitude'])
    lalos = [] # LALOS  # to be replaced by database add / database query
    lalos.append(_me)

    dists = [haversine(targ, lalo) for lalo in lalos]
    me['dists'] = dists
    print me
    return jsonify(result=me.values(), dists=dists)


@proj.route('/_add_tee')
def _add_tee():
    print request.args
    print request.args.values()
    # DATABASE: add email invite to our rV group
    return jsonify(result=request.args.values())
