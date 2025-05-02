from flask import Flask
import folium

app = Flask(__name__)

@app.route("/")
def base():
    map = folium.Map(
        location=[-22.522814, -44.123209], #mapa inicial
        zoom_start=15
    )

    folium.Marker(
        location=[-22.496805, -44.139830],
        popup="<b>12 Furtos 3 Roubos<b/>",
        tooltip="<b>Açude</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)
    
    folium.Marker(
        location=[-22.494688, -44.135350],
        popup="<b>3 Furtos 1 Roubo<b/>",
        tooltip="<b>Açude 2</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.503992, -44.138072],
        popup="<b>3 Furtos<b/>",
        tooltip="<b>Açude 3</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.507044, -44.088481],
        popup="<b>325 Furtos 57 Roubos<b/>",
        tooltip="<b>Aterrado</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.503113, -44.081076],
        popup="<b>68 Furtos 13 Roubos<b/>",
        tooltip="<b>Aero Clube</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.507950, -44.068231],
        popup="<b>44 Furtos 11 Roubos<b/>",
        tooltip="<b>Água Limpa</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.494617, -44.086202],
        popup="<b>5 Furtos 2 Roubos<b/>",
        tooltip="<b>Barreira Cravo</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.524261, -44.109158],
        popup="<b>6 Furtos 3 Roubos<b/>",
        tooltip="<b>Bela Vista</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.510170, -44.134735],
        popup="<b>23 Furtos 4 Roubos<b/>",
        tooltip="<b>Belmonte</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.490610, -44.121331],
        popup="<b>6 Furtos<b/>",
        tooltip="<b>Belo Horizonte</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.495095, -44.106850],
        popup="<b>13 Furtos 2 Roubos<b/>",
        tooltip="<b>Bom Jesus</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.482872, -44.061448],
        popup="<b>9 Furtos 1 Roubo<b/>",
        tooltip="<b>Brasilandia</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.479854, -44.058105],
        popup="<b>4 Furtos Roubos<b/>",
        tooltip="<b>Caieira</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.481532, -44.059798],
        popup="<b>1 Furto<b/>",
        tooltip="<b>Cailandia</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.471693, -44.075729],
        popup="<b>1 Furto 1 Roubo<b/>",
        tooltip="<b>Candelaria</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.539327, -44.078451],
        popup="<b>8 Furtos 5 Roubos<b/>",
        tooltip="<b>Casa de Pedra</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.512789, -44.091216],
        popup="<b>167 Furtos 21 Roubos<b/>",
        tooltip="<b>Centro</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.494435, -44.041321],
        popup="<b>5 Furtos<b/>",
        tooltip="<b>Colorado</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.522814, -44.123208],
        popup="<b>109 Furtos 29 Roubos<b/>",
        tooltip="<b>Conforto</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.491720, -44.108243],
        popup="<b>2 Furtos<b/>",
        tooltip="<b>Coqueiros</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.475690, -44.059073],
        popup="<b>22 Furtos 1 Roubo<b/>",
        tooltip="<b>Dom Bosco</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.529989, -44.127392],
        popup="<b>14 Furtos<b/>",
        tooltip="<b>Duzentos e quarenta e nove</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.493226, -44.103987],
        popup="<b>3 Furtos<b/>",
        tooltip="<b>Eldorado</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.525966, -44.120233],
        popup="<b>23 Furtos 2 Roubos<b/>",
        tooltip="<b>Eucaliptal</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.486929, -44.105845],
        popup="<b>1 Furto<b/>",
        tooltip="<b>Fazendinha</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.487173, -44.086668],
        popup="<b>1 Roubo<b/>",
        tooltip="<b>Ilha parque</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.489794, -44.089530],
        popup="<b>2 Furtos<b/>",
        tooltip="<b>Ilha São João</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.510241, -44.081521],
        popup="<b>101 Furtos 25 Roubos<b/>",
        tooltip="<b>Jardim amalia</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.532705, -44.070768],
        popup="<b>12 Furtos 2 Roubos<b/>",
        tooltip="<b>Jardim Belvedere</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.504235, -44.120962],
        popup="<b>7 Furtos 5 Roubos<b/>",
        tooltip="<b>Jardim Cidade do Aço</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.532717, -44.087594],
        popup="<b>1 Roubo<b/>",
        tooltip="<b>Jardim Esperança</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.528293, -44.130533],
        popup="<b>4 Furtos 2 Roubos<b/>",
        tooltip="<b>Jardim Europa</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.513489, -44.083039],
        popup="<b>16 Furtos 1 Roubo<b/>",
        tooltip="<b>Jardim Normandia</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.515264, -44.146800],
        popup="<b>3 Furtos 1 Roubo<b/>",
        tooltip="<b>Jardim Padre Josimo Tavares</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.509976, -44.097975],
        popup="<b>30 Furtos 5 Roubos<b/>",
        tooltip="<b>Jardim Paraiba</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.534220, -44.129250],
        popup="<b>2 Furtos<b/>",
        tooltip="<b>Jardim Ponte Alta</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.497349, -44.096405],
        popup="<b>8 Furtos<b/>",
        tooltip="<b>Jardim Primavera</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.535033, -44.136541],
        popup="<b>2 Furtos<b/>",
        tooltip="<b>Jardim Suiça</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.544776, -44.067288],
        popup="<b>41 Furtos 13 Roubos<b/>",
        tooltip="<b>Jardim Vila Rica - Tiradentes</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.519329, -44.098299],
        popup="<b>32 Furtos 12 Roubos<b/>",
        tooltip="<b>Laranjal</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.495528, -44.099863],
        popup="<b>4 Furtos<b/>",
        tooltip="<b>Limoeiro</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.490147, -44.107165],
        popup="<b>3 Furtos 1 Roubo<b/>",
        tooltip="<b>Mariana Torres</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.534310, -44.123376],
        popup="<b>9 Furtos 4 Roubos<b/>",
        tooltip="<b>Minerlândia</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.491806, -44.097213],
        popup="<b>1 Furto<b/>",
        tooltip="<b>Mirante do Vale</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.520953, -44.091142],
        popup="<b>20 Furtos 5 Roubos<b/>",
        tooltip="<b>Monte Castelo</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.512885, -44.072462],
        popup="<b>5 Furtos<b/>",
        tooltip="<b>Morada da Colina</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.492410, -44.071071],
        popup="<b>6 Furtos<b/>",
        tooltip="<b>Morro da Conquista</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.530472, -44.124995],
        popup="<b>5 Furtos<b/>",
        tooltip="<b>Morro do São Carlos</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)
    
    folium.Marker(
        location=[-22.498770, -44.091970],
        popup="<b>20 Furtos 5 Roubos<b/>",
        tooltip="<b>Niterói</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.503169, -44.094865],
        popup="<b>21 Furtos 8 Roubos<b/>",
        tooltip="<b>Nossa Senhora das Graças</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.488264, -44.120369],
        popup="<b>4 Furtos<b/>",
        tooltip="<b>Nova Esperança</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.486664, -44.054965],
        popup="<b>7 Furtos<b/>",
        tooltip="<b>Nova Primavera</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.490032, -44.084736],
        popup="<b>2 Furtos<b/>",
        tooltip="<b>Parque das ilhas</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.528708, -44.135227],
        popup="<b>35 Furtos 16 Roubos<b/>",
        tooltip="<b>Ponte Alta</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.500317, -44.124394],
        popup="<b>214 Furtos 44 Roubos<b/>",
        tooltip="<b>Retiro</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.590325, -44.074973],
        popup="<b>11 Furtos 4 Roubos<b/>",
        tooltip="<b>Rio das Flores</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.599528, -44.078390],
        popup="<b>25 Furtos 10 Roubos<b/>",
        tooltip="<b>Roma</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)


    folium.Marker(
        location=[-22.522622, -44.112855],
        popup="<b>3 Furtos 1 Roubo<b/>",
        tooltip="<b>Rústico</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.495156, -44.084335],
        popup="<b>7 Furtos 2 Roubos<b/>",
        tooltip="<b>San Remo</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.464588, -44.096144],
        popup="<b>18 Furtos 3 Roubos<b/>",
        tooltip="<b>Santa Cruz</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.464622, -44.101245],
        popup="<b>11 Furtos<b/>",
        tooltip="<b>Santa Cruz 2</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.532576, -44.115421],
        popup="<b>2 Furtos 1 Roubo<b/>",
        tooltip="<b>Santa Inês</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.465892, -44.110494],
        popup="<b>12 Furtos 3 Roubos<b/>",
        tooltip="<b>Santa Rita do Zarur</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.523453, -44.112855],
        popup="<b>1 Roubo<b/>",
        tooltip="<b>Santa Tereza</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.487394, -44.077056],
        popup="<b>97 Furtos 10 Roubos<b/>",
        tooltip="<b>Santo Agostinho</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.533353, -44.118602],
        popup="<b>14 Furtos 1 Roubo<b/>",
        tooltip="<b>São Cristovão</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.516800, -44.086030],
        popup="<b>129 Furtos 16 Rouboss<b/>",
        tooltip="<b>São Geraldo</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.516180, -44.091420],
        popup="<b>65 Furtos 6 Roubos<b/>",
        tooltip="<b>São João</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.485664, -44.098887],
        popup="<b>2 Furtos 2 Roubos<b/>",
        tooltip="<b>São João Batista</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.529968, -44.120030],
        popup="<b>42 Furtos 6 Roubos<b/>",
        tooltip="<b>São Lucas</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.475577, -44.065528],
        popup="<b>44 Furtos 7 Roubos<b/>",
        tooltip="<b>São Luís</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.463774, -44.062028],
        popup="<b>8 Furtos 2 Roubos<b/>",
        tooltip="<b>São Sebastião</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.524360, -44.095648],
        popup="<b>24 Furtos 4 Roubos<b/>",
        tooltip="<b>Sessenta</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.521308, -44.139994],
        popup="<b>27 Furtos 6 Roubos<b/>",
        tooltip="<b>Siderlândia</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.538078, -44.086678],
        popup="<b>4 Furtos 3 Roubos<b/>",
        tooltip="<b>Siderópolis</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.496374, -44.041063],
        popup="<b>26 Furtos 13 Roubos<b/>",
        tooltip="<b>Três poços</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.492561, -44.113637],
        popup="<b>4 Roubos<b/>",
        tooltip="<b>Vale Verde</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.499579, -44.074654],
        popup="<b>33 Furtos 13 Roubos<b/>",
        tooltip="<b>Vila Americana</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.486368, -44.109348],
        popup="<b>18 Furtos 1 Roubo<b/>",
        tooltip="<b>Vila Brasilia</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[--22.499883, -44.104309],
        popup="<b>77 Furtos 24 Roubos<b/>",
        tooltip="<b>Vila Mury</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)


    folium.Marker(
        location=[-22.521873, -44.103138],
        popup="<b>275 Furtos 47 Roubos<b/>",
        tooltip="<b>Vila Santa Cecília</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.534948, -44.072089],
        popup="<b>2 Furtos<b/>",
        tooltip="<b>Vilage Sul</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.491864, -44.092963],
        popup="<b>52 Furtos 9 Roubos<b/>",
        tooltip="<b>Voldac</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    folium.Marker(
        location=[-22.485655, -44.077675],
        popup="<b>7 Furtos<b/>",
        tooltip="<b>Volta Grande</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)


    folium.Marker(
        location=[-22.486535, -44.071940],
        popup="<b> furtos e  roubos<b/>",
        tooltip="<b>Volta Grande 2</b>",
        icon=folium.Icon(icon="circle", color="red", prefix="fa")
    ).add_to(map)

    











    return map._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)