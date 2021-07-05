from weatherreport.dashboard import Dashboard
from weatherreport.weather import Weather

if __name__ == '__main__':
    mainDashboard = Dashboard('Main')
    mobileDashboard = Dashboard('Mobile')

    weatherDublin = Weather('Dublin')
    weatherMadrid = Weather('Madrid')
    weatherNY = Weather('New York')

    # mobileDashboard is interested in the climate of only two cities
    weatherNY.attach_observer(mobileDashboard)
    weatherDublin.attach_observer(mobileDashboard)

    weatherDublin.attach_observer(mainDashboard)
    weatherMadrid.attach_observer(mainDashboard)
    weatherNY.attach_observer(mainDashboard)

    #changes happends and observers are notified
    weatherMadrid.notify_change("27°C")
    weatherDublin.notify_change("15°C")
    weatherNY.notify_change("9°C")

    #remove observer and watch again other changes
    print('removing observer from weatherNY')
    weatherNY.remove_observer(mainDashboard)
    weatherMadrid.notify_change("26°C")
    weatherDublin.notify_change("14°C")
    weatherNY.notify_change("8°C")



