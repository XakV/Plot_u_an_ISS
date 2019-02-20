import requests
import plotly.plotly as py
import plotly.graph_objs as go

def where_is_iss():
    iss_loc = requests.get('http://api.open-notify.org/iss-now.json')
    iss_string = iss_loc.json()
    iss_s_dict = iss_string['iss_position']
    return iss_s_dict

def show_where_that_is(lat, long):
    mapbox_access_token = "get a secret token"
    data = [go.Scattermapbox(lat=[lat], lon=[long], mode='markers', marker=dict(size=14), text=['ISS'],)]
    layout = go.Layout(autosize=True, hovermode='closest', mapbox=dict(
        accesstoken=mapbox_access_token, bearing=0, center=dict(lat=lat, lon=long), pitch=0, zoom=5),)
    fig = dict(data=data, layout=layout)
    py.iplot(fig, filename='ISS')

def main():
    iss_loc = where_is_iss()
    iss_lat = float(iss_loc['latitude'])
    iss_long = float(iss_loc['longitude'])
    show_where_that_is(iss_lat, iss_long)

if __name__ == '__main__':
    main()
