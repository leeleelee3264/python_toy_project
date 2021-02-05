import dash

# dash app container
external_stylesheets = ['/assets/css/dash.css']

my_app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
my_app.config.suppress_callback_exceptions = True