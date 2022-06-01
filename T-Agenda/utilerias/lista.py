from utilerias.clases import Empleado
import tkinter as tk
from tkinter import W, ttk
from tkinter.font import BOLD, ITALIC
from tkinter.tix import COLUMN

class Node:
  def __init__(self, data:Empleado):
    self.data = data
    self.next = self

  def __repr__ (self):
    return str(self.data)

class CLL:
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0

  def __repr__(self):
    string = ""

    if (self.head == None):
      string += "CLL empty"
      return string
    
    string += f"CLL list: \n{self.head.data}" # PTR
    P = self.head.next # Segundo nodo despues de PTR
    while(P != self.head):
      string += f" -> {P.__str__()}"
      P = P.next
    return string

  def insert(self, value):

    if(self.head == None):
      self.head = Node(value)
      self.tail = self.head
    else:
      self.tail.next = Node(value)
      self.tail = self.tail.next
      self.tail.next = self.head

  def buscar(self, user, pas):
    current = self.head
    encontrado = False
    person=None
    while (current.next != self.head and encontrado==False):
      
      if(current.data.name == user and current.data.contra==pas):
        encontrado= True
        person=current.data
      else:
        current=current.next
    return person
  
  def buscarporCedula(self, cedul):
    current = self.head
    encontrado = False
    trabajador = None
    while (current.next != self.head and encontrado==False):
      
      if(current.data.cedula == cedul ):
        encontrado= True
        trabajador=current.data
      else:
        current= current.next
        trabajador= -1
    return trabajador

  def mostrarHorario(self, dia, Tx:tk.Text):
    current = self.head
    while (current.next != self.head ):
      current.data.recorTurnos(dia, Tx)
      current = current.next

      