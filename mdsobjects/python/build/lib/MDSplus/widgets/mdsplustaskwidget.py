from gtk import VBox
from MDSplus.widgets.mdspluserrormsg import MDSplusErrorMsg
from MDSplus.widgets.mdsplusexpressionwidget import MDSplusExpressionWidget
from MDSplus.widgets.mdsplusroutinewidget import MDSplusRoutineWidget
from MDSplus.widgets.mdsplusmethodwidget import MDSplusMethodWidget
from MDSplus.widgets.mdsplusdtypeselwidget import MDSplusDtypeSelWidget


class MDSplusTaskWidget(MDSplusDtypeSelWidget,VBox):

    def __init__(self):
        super(MDSplusTaskWidget,self).__init__(homogeneous=False,spacing=10)
        menu=self.dtype_menu(("Method","Routine"))
        self.method=MDSplusMethodWidget()
        self.routine=MDSplusRoutineWidget()
        self.routine.set_no_show_all(True)
        self.expression=MDSplusExpressionWidget()
        self.expression.set_no_show_all(True)
        self.widgets=(self.method,self.routine,self.expression)
        self.pack_start(menu,False,False,0)
        self.pack_start(self.method,True,True,0)
        self.pack_start(self.routine,True,True,0)
        self.pack_start(self.expression,True,True,0)
