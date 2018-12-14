# import the library
from appJar import gui

#from simpleeditor.simpleeditor import launch_editor

import sys, time
import subprocess
import configparser
import json

from_pid, to_pid, pids_step = (0, 0, 0)
retrieval_params = {}

retrievalConfigFile = './retrieval_config.ini'
importConfigFile = './import_config.json'


def logoutFunction():
    '''
    Function to confirm logout
    '''
    retval = app.yesNoBox('Confirm Exit', 'Are you sure you want to exit?')
    if retval == 'yes':
        app.destroySubWindow('editor')
    return retval


def showTime():
    '''
    Function to update status bar with the time
    '''
    app.setStatusbar(time.strftime('%X'))

    
def press(button):
    '''
    Handle button events
    '''
    if button == 'Cancel':
        app.stop()
    else:
        usr = app.getEntry('Username')
        pwd = app.getEntry('Password')
        print('User:', usr, 'Pass:', pwd)

        
def set_pid_range(name):
    '''
    Defines from_pid and to_pid
    '''
    global from_pid, to_pid
    if name == 'spinFromPid':
        from_pid = int(app.getSpinBox(name))
        if from_pid > to_pid:
            to_pid = from_pid
            app.setSpinBox('spinToPid', to_pid)
    else:
        to_pid = int(app.getSpinBox(name))
        if to_pid < from_pid:
            from_pid = to_pid
            app.setSpinBox('spinFromPid', to_pid)

            
def set_year(name):
    pass


def set_month(name):
    pass


def set_day(name):
    pass


def set_doy(name):
    pass


def set_hour(name):
    pass


def set_min(name):
    pass


def set_sec(name):
    pass


def set_msec(name):
    pass


def radbtnExportDateTime(name):
    '''
    Get actual value of date time, depending on the input data
    '''
    if name == 'radFromYMDorYDOY':
        if app.getRadioButton('radFromYMDorYDOY') == 'Y-M-D':
            app.enableSpinBox('spinFromYMDy')
            app.enableSpinBox('spinFromYMDm')
            app.enableSpinBox('spinFromYMDd')
            app.disableSpinBox('spinFromYDoYy')
            app.disableSpinBox('spinFromYDoYdoy')
        else:
            app.disableSpinBox('spinFromYMDy')
            app.disableSpinBox('spinFromYMDm')
            app.disableSpinBox('spinFromYMDd')
            app.enableSpinBox('spinFromYDoYy')
            app.enableSpinBox('spinFromYDoYdoy')
    elif name == 'radToYMDorYDOY':
        if app.getRadioButton('radToYMDorYDOY') == 'Y-M-D':
            app.enableSpinBox('spinToYMDy')
            app.enableSpinBox('spinToYMDm')
            app.enableSpinBox('spinToYMDd')
            app.disableSpinBox('spinToYDoYy')
            app.disableSpinBox('spinToYDoYdoy')
        else:
            app.disableSpinBox('spinToYMDy')
            app.disableSpinBox('spinToYMDm')
            app.disableSpinBox('spinToYMDd')
            app.enableSpinBox('spinToYDoYy')
            app.enableSpinBox('spinToYDoYdoy')

            
def get_retrieval_params():
    '''
    Get JSON object with the current retrieval configuration parameters
    '''
    return {
        'from_pid': app.getSpinBox('spinFromPid'),
        'to_pid': app.getSpinBox('spinToPid'),
        'pids_step': app.getSpinBox('spinStepPid'),
        'from_date_time': {
            'mode': ('ymd' if app.getRadioButton('radFromYMDorYDOY') == 'Y-M-D' else 'ydoy'),
            'ymd': [
                app.getSpinBox('spinFromYMDy'),
                app.getSpinBox('spinFromYMDm'),
                app.getSpinBox('spinFromYMDd')
            ],
            'ydoy': [
                app.getSpinBox('spinFromYDoYy'),
                app.getSpinBox('spinFromYDoYdoy')
            ],
            'time': [
                app.getSpinBox('spinFromH'),
                app.getSpinBox('spinFromM'),
                app.getSpinBox('spinFromS'),
                app.getSpinBox('spinFromMS')
            ]
        },
        'to_date_time': {
            'mode': ('ymd' if app.getRadioButton('radToYMDorYDOY') == 'Y-M-D' else 'ydoy'),
            'ymd': [
                app.getSpinBox('spinToYMDy'),
                app.getSpinBox('spinToYMDm'),
                app.getSpinBox('spinToYMDd')
            ],
            'ydoy': [
                app.getSpinBox('spinToYDoYy'),
                app.getSpinBox('spinToYDoYdoy')
            ],
            'time': [
                app.getSpinBox('spinToH'),
                app.getSpinBox('spinToM'),
                app.getSpinBox('spinToS'),
                app.getSpinBox('spinToMS')
            ]
        }
    }


def go_retrieve():
    '''
    Perform actual retrieve
    '''
    print(get_retrieval_params())
    app.showFrame('retrieveResults')

    #result = subprocess.run(['cat', 'test6.log'], stdout=subprocess.PIPE)

    cmd = "bash dryrun.sh"
    #cmd = "/usr/sbin/netstat -p tcp -f inet"
    output = ''
 
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    while True:
        out = p.stdout.readline().decode('utf-8')
        if out == '' and p.poll() != None:
            break
        if out != '':
            sys.stdout.write(out)
            sys.stdout.flush()
            output = output + out
            app.setMessage('retrieveLog', output)

    app.stop()

    
def go_import():
    '''
    Perform actual import
    '''
    app.stop()


def launch_editor(file=None):
    '''
    Show editor dialog
    '''
    with open(file, 'r') as f:
        f_data = f.read()
    app.setTextArea('editorArea', f_data)
    app.showSubWindow('editor')


def editMenu(btn):
    print(btn)


def go_edit_retrieval_cfgfile():
    '''
    Edit the retrieval config file in an external application
    '''
    launch_editor(file=retrievalConfigFile)


def go_edit_import_cfgfile():
    '''
    Edit the retrieval config file in an external application
    '''
    launch_editor(file=importConfigFile)


def show_retrieval_config_file(wdg):
    '''
    Display configuration from retrieval config. file
    '''

    ## Retrieval configuration
    #retr_config = configparser.ConfigParser()
    #retr_data = retr_config.read(retrievalConfigFile)
    with open(retrievalConfigFile, 'r') as retr:
        retr_data = retr.read()
    app.setTextArea(wdg, retr_data)


def show_import_config_file(wdg):
    '''
    Display configuration from import config. file
    '''
    ## Import configuration
    with open(importConfigFile, 'r') as imprt:
        imprt_data = json.load(imprt)
    imprtContent = json.dumps(imprt_data, indent=4)
    app.setTextArea(wdg, imprtContent)


#def main():
#    '''
#    Main processor program
#    '''

# create a GUI variable called app
app = gui('ARES IE Tool')

# Splash
#app.showSplash('ARES Import/Export Tool')

app.setFont(size=9)
#app.setFg('white', override=True)
#app.setBg('#204040', override=False, tint=True)

##------------------------------------------------------------
## Define main window
##------------------------------------------------------------

# Statusbar to show the time
app.addStatusbar(side='RIGHT')
app.registerEvent(showTime)
app.stopFunction = logoutFunction

# Tabs
with app.tabbedFrame('Tabs'):lf.
    app.setPadding([6,6])

    #----------------------------------------------------------------------

    with app.tab('Retrieve from ARES'):
        app.setPadding([6,6])
        app.stretch='column'

        app.addLabelEntry('Applicable retrieval config. file:');
        app.setEntry('Applicable retrieval config. file:',
                     retrievalConfigFile, callFunction=False)
        app.disableEntry('Applicable retrieval config. file:')

        #app.setLabelEntryAlign('lblCfg', 'left')

        with app.labelFrame('Retrieval parameters', colspan=3, sticky='ew'):
            app.setPadding([6,6])

            with app.labelFrame('Parameter identifiers'):
                app.setPadding([6,6])

                app.label('lblFromPid', 'From Param. Id.', sticky='news')
                app.setLabelAlign('lblFromPid', 'left')
                app.spin('spinFromPid', row='p', column=1, width=8,
                         value=1, endValue=50000, item='1',
                         change=set_pid_range, focus=True)

                app.label('lblToPid', 'To Param. Id.', row='p', column=2, sticky='news')
                app.setLabelAlign('lblToPid', 'left')
                app.spin('spinToPid', row='p', column=3, width=8,
                         value=1, endValue=50000, item='1000',
                         change=set_pid_range)

                app.label('lblStepPid', 'Param. Id. Block Size (for FITS files)',
                          colspan=2, sticky='news')
                app.setLabelAlign('lblStepPid', 'left')
                app.spin('spinStepPid', row='p', column=2, width=8,
                         value=1, endValue=20000, item='1000')

            with app.labelFrame('Date range'):
                app.setPadding([6,6])

                with app.frame('fromTimestamp'):
                    app.setPadding([6,6])

                    app.label('lblFromTimestamp', 'From Timestamp', width=14)
                    app.setLabelAlign('lblFromTimestamp', 'left')

                    with app.frame('fromTSdate', row='p', column=1):
                        app.setPadding([2,2])

                        app.radio('radFromYMDorYDOY', 'Y-M-D')
                        with app.frame('fromTS_YMD', row='p', column=1):
                            app.spin('spinFromYMDy', width=6, value=2010, endValue=2100, item='2018', change=set_year)
                            app.label('lblFromYHip', '-', width=1, row='p', column=1)
                            app.spin('spinFromYMDm', width=3, row='p', column=2, value=1, endValue=12, item='1', change=set_month)
                            app.label('lblFromMHip', '-', width=1, row='p', column=3)
                            app.spin('spinFromYMDd', width=3, row='p', column=4, value=1, endValue=31, item='1', change=set_day)

                        app.radio('radFromYMDorYDOY', 'Y.DoY')
                        with app.frame('fromTS_YDOY', row='p', column=1):
                            app.spin('spinFromYDoYy', width=6, value=2010, endValue=2100, item='2018', change=set_year)
                            app.label('lblFromDoYDot', '.', width=1, row='p', column=1)
                            app.spin('spinFromYDoYdoy', width=4, row='p', column=2, value=1, endValue=366, item='1', change=set_doy)

                        app.setRadioButtonChangeFunction('radFromYMDorYDOY', radbtnExportDateTime)
                        app.setRadioButton('radFromYMDorYDOY', 'Y-M-D')

                    with app.frame('fromTStime', row='p', column=2):
                        app.spin('spinFromH', width=3, value=0, endValue=23, item='0', change=set_hour, sticky='ew')
                        app.label('lblFromhCol', ':', width=1, row='p', column=1)
                        app.spin('spinFromM', width=3, row='p', column=2, value=0, endValue=59, item='0', change=set_min)
                        app.label('lblFrommCol', ':', width=1, row='p', column=3)
                        app.spin('spinFromS', width=3, row='p', column=4, value=0, endValue=59, item='0', change=set_sec)
                        app.label('lblFromsDot', '.', width=1, row='p', column=5)
                        app.spin('spinFromMS', width=4, row='p', column=6, value=0, endValue=999, item='0', change=set_msec)

                with app.frame('toTimestamp'):
                    app.setPadding([6,6])

                    app.label('lblToTimestamp', 'To Timestamp', width=14)
                    app.setLabelAlign('lblToTimestamp', 'left')

                    with app.frame('toTSdate', row='p', column=1):
                        app.setPadding([2,2])

                        app.radio('radToYMDorYDOY', 'Y-M-D')
                        with app.frame('toTS_YMD', row='p', column=1):
                            app.spin('spinToYMDy', width=6, value=2010, endValue=2100, item='2018', change=set_year)
                            app.label('lblToYHip', '-', width=1, row='p', column=1)
                            app.spin('spinToYMDm', width=3, row='p', column=2, value=1, endValue=12, item='1', change=set_month)
                            app.label('lblToMHip', '-', width=1, row='p', column=3)
                            app.spin('spinToYMDd', width=3, row='p', column=4, value=1, endValue=31, item='1', change=set_day)

                        app.radio('radToYMDorYDOY', 'Y.DoY')
                        with app.frame('toTS_YDOY', row='p', column=1):
                            app.spin('spinToYDoYy', width=6, value=2010, endValue=2100, item='2018', change=set_year)
                            app.label('lblToDoYDot', '.', width=1, row='p', column=1)
                            app.spin('spinToYDoYdoy', width=4, row='p', column=2, value=1, endValue=366, item='1', change=set_doy)

                        app.setRadioButtonChangeFunction('radToYMDorYDOY', radbtnExportDateTime)
                        app.setRadioButton('radToYMDorYDOY', 'Y-M-D')

                    with app.frame('toTStime', row='p', column=2):
                        app.spin('spinToH', width=3, value=0, endValue=23, item='0', change=set_hour, sticky='ew')
                        app.label('lblTohCol', ':', width=1, row='p', column=1)
                        app.spin('spinToM', width=3, row='p', column=2, value=0, endValue=59, item='0', change=set_min)
                        app.label('lblTomCol', ':', width=1, row='p', column=3)
                        app.spin('spinToS', width=3, row='p', column=4, value=0, endValue=59, item='0', change=set_sec)
                        app.label('lblTosDot', '.', width=1, row='p', column=5)
                        app.spin('spinToMS', width=4, row='p', column=6, value=0, endValue=999, item='0', change=set_msec)

        with app.frame('retrieveButton'):
            app.setPadding([6,6])

            app.label('nolbl1wide', '', stretch='both') #, sticky='ew')

            app.label('nolbl1', '')
            app.button('Retrieve data', go_retrieve, pos='p', sticky='nes', stretch='column')

        with app.frame('retrieveResults'):
            app.setPadding([6,6])

            app.startScrollPane('RETRIEVE_PANE', sticky='ew')
            app.message('retrieveLog', '', sticky='ew')
            app.stopScrollPane()

        app.hideFrame('retrieveResults')

    #----------------------------------------------------------------------

    with app.tab('Import into ARES'):
        app.setPadding([6,6])
        app.stretch='column'

        app.addLabelEntry('Applicable import parameters config. file:')
        app.setEntry('Applicable import parameters config. file:',
                     importConfigFile, callFunction=False)
        app.disableEntry('Applicable import parameters config. file:')

        with app.labelFrame('Import parameters', colspan=3, sticky='ew'):
            app.setPadding([6,6])

            app.label('dummy2', 'To Timestamp', width=14)
            app.setLabelAlign('dummy2', 'left')

        app.label('nolbl2wide', '', stretch='both') #, sticky='ew')

        app.label('nolbl2', '')
        app.button('Import data', go_import, pos='p', sticky='nes', stretch='column')

    #----------------------------------------------------------------------

    with app.tab('Configuration'):
        app.setPadding([6,6])
        app.stretch='column'
        
        app.startPanedFrame('configPane1', sticky='ns')

        with app.labelFrame('Retrieval config. file'):
            app.setPadding([6,6])
            app.addFileEntry('retrievalIniFile')
            app.setEntry('retrievalIniFile', retrievalConfigFile)

            app.addTextArea('txtRetrieval')
            show_retrieval_config_file('txtRetrieval')
            app.setTextAreaFont('txtRetrieval', size=8)
            app.setTextAreaWidth('txtRetrieval', 60)

            with app.frame('editRetrCfgBtn'):
                app.setPadding([6,6])
                app.label('nolbl31wide', '', stretch='both') #, sticky='ew')
                app.button('Edit Retrieval config file', go_edit_retrieval_cfgfile, sticky='nes', stretch='column')

        app.startPanedFrame('configPane2')

        with app.labelFrame('Import config. file'):
            app.setPadding([6,6])
            app.addFileEntry('importIniFile')
            app.setEntry('importIniFile', importConfigFile)

            app.addTextArea('txtImport')
            show_import_config_file('txtImport')
            app.setTextAreaFont('txtImport', size=8)
            app.setTextAreaWidth('txtImport', 60)
            
            with app.frame('editImprtCfgBtn'):
                app.setPadding([6,6])
                app.label('nolbl32wide', '', stretch='both') #, sticky='ew')
                app.button('Edit Import config file', go_edit_import_cfgfile, sticky='nes', stretch='column')

        app.stopPanedFrame()
        app.stopPanedFrame()


##------------------------------------------------------------
## Define editor sub-window
##------------------------------------------------------------
with app.subWindow('editor', modal=True, transient=True, sticky='news'):
    ## Menu
    app.startFrame('editorMenu', 0, 0, colspan=5)
    app.setStretch('both')

    app.button('OPEN', editMenu, label='Open', column=0, sticky='nes')
    app.button('SAVE', editMenu, label='Save', pos='p', column=1, sticky='nes')
    app.button('SAVEAS', editMenu, label='Save As...', pos='p', column=2, sticky='nes')
    app.button('CLOSE', editMenu, label='Close', pos='p', column=5, sticky='nws')
    
    app.stopFrame()
    
    ## Area
    app.setSticky('news')
    app.textArea('editorArea', sticky="news", colspan=5)
    app.setTextAreaFont('editorArea', size=8)
    

# start the GUI
app.go()

#if __name__ == '__main__':
#    main()
#    
