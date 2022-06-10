def cliente (d):
    respuesta = {}
    respuesta ["nombre"]= d["nombre"]
    respuesta ["edad"]= d["edad"]
#xtreme
    if d ["edad"] >18:
        respuesta ["atraccion"]="X-Treme"    
        respuesta ["apto"] =True
        respuesta ["primer_ingreso"]= d["primer_ingreso"]
        if d ["primer_ingreso"]==True:
          respuesta ["total_boleta"]=20000-20000*0.05
        else:
            respuesta ["total_boleta"]=20000
#chocones        
    elif d["edad"] >=15 and d["edad"]<=18:
        respuesta ["atraccion"] = "Carros chocones"
        respuesta ["apto"] = True
        respuesta ["primer_ingreso"]= d["primer_ingreso"]
        if d ["primer_ingreso"]==True:
          respuesta ["total_boleta"]=5000-5000*0.07
        else:
            respuesta ["total_boleta"]=5000

#sillas voladoras 
    elif d["edad"] >=7 and d ["edad"] <15:
      respuesta ["atraccion"]="Sillas voladoras"
      respuesta ["apto"]= True
      respuesta ["primer_ingreso"]= d["primer_ingreso"]
      if d ["primer_ingreso"]==True:
          respuesta ["total_boleta"]=10000-10000*0.05
      else:
          respuesta ["total_boleta"]=10000

#No cumple

    else:
      respuesta ["atraccion"] = "N/A"
      respuesta ["apto"]= False
      respuesta ["primer_ingreso"]= d["primer_ingreso"]
      respuesta ["total_boleta"] = "N/A"
      
    return respuesta

#Código principal
dic1={"id_cliente":1,"nombre":"Johana Fernandez", "edad":20, "primer_ingreso":True}
dic2={"id_cliente":1,"nombre":"Johana Fernandez", "edad":20, "primer_ingreso":False}
dic3={"id_cliente":2,"nombre":"Gloria Suarez", "edad":3, "primer_ingreso":True}
dic4={"id_cliente":3,"nombre":"Tatiana Suarez", "edad":17, "primer_ingreso":True}
dic5={"id_cliente":3,"nombre":"Tatiana Suarez", "edad":17, "primer_ingreso":False}
dic6={"id_cliente":4,"nombre":"Tatiana Ruiz", "edad":8, "primer_ingreso":True}
dic7={"id_cliente":4,"nombre":"Tatiana Ruiz", "edad":8, "primer_ingreso":False}


print(cliente(dic1))
print(cliente(dic2))
print(cliente(dic3))
print(cliente(dic4))
print(cliente(dic5))
print(cliente(dic6))
print(cliente(dic7))