import flet as ft
import operator

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno=None
        self._stato=None

    def handleAnno(self, e):
        value = e.control.value
        if value.strip().isdigit():
            anno = int(value)
            if 1816 <= anno <= 2016:
                self._anno = anno
            else:
                self._anno = None
        else:
            self._anno = None
    def handleCalcola(self, e):
        if not self._anno:
            self._view.create_alert("L'anno inserito è sbagliato o non è stato inserito alcun anno")
            return
        self._model.creaGrafo(self._anno)
        dizio=self._model.getinfoNodi()
        dizio=dict(sorted(dizio.items(),key=lambda x:x[0].StateNme))
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Grafo creato correttamente\n\nIl grafo ha {self._model.componenti_connesse()} componenti connesse\n\nDi seguito i dettagli sui nodi: "))
        for key in dizio.keys():
            self._view._txt_result.controls.append(ft.Text(f"{key.StateNme} -- {dizio[key]} vicini"))
        self.dd_fill()
        self._view.update_page()
    def handleStato(self, e):
        if e.control.data:
            self._stato=e.control.data
        else:
            self._stato=None
    def handleRaggiungi(self,e):
        if not self._stato:
            self._view.create_alert("Non hai inserito nessuno Stato")
            return
        visited=self._model.getBFSnodes(self._stato)
        self._view._txt_result.controls.clear()
        if len(visited)==0:
            self._view._txt_result.controls.append(ft.Text(f"Dallo stato chiamato {self._stato.StateNme} non si possono raggiungere altri stati via terra in anno {self._anno}"))

        else:
            self._view._txt_result.controls.append(ft.Text(f"Dallo stato chiamato {self._stato.StateNme}  si possono raggiungere i seguenti stati via terra in anno {self._anno}"))
            for element in visited:
                self._view._txt_result.controls.append(ft.Text(f"{element.StateNme}"))
        self._view.update_page()
    def dd_fill(self):
        self._view._dd_Stati.disabled=False
        self._view._dd_Stati.clean()
        self._view._btn_Raggiungibili.disabled=False
        dizio=self._model.getinfoNodi()
        for key in dizio.keys():
            self._view._dd_Stati.options.append(ft.dropdown.Option(text=key.StateNme,
                                                 data=key,
                                                 on_click=self.handleStato))

