import streamlit as st
import pandas as pd

st.set_page_config(page_title='Evaluación Riesgos IA', layout='wide')

st.title('Sistema de Evaluación de Riesgos para Sistemas de IA Aplicado a Ciberseguridad')

# Fase 1
st.header('1) Identificación del Sistema')
nombre = st.text_input('Nombre del Sistema')

sistemas = {
    'Sistema de Detección de Phishing':1,
    'Sistema de Detección de Intrusos':2,
    'Sistemas Utilizados en Centros de Operaciones de Seguridad (SOC)':2,
    'Sistema de Detección de Fraude':3
}
TS_label = st.selectbox('Tipo de Sistema', list(sistemas.keys()))
TS = sistemas[TS_label]
TD = {'No Sensibles':1,'Sensibles':2}[st.selectbox('Tipo de Datos',['No Sensibles','Sensibles'])]
NA = {'Asistido':1,'Semiautomático':2,'Automático':3}[st.selectbox('Nivel de Automatización',['Asistido','Semiautomático','Automático'])]
CU = {'Empresarial':1,'Regulatorio':2}[st.selectbox('Contexto de Uso',['Empresarial','Regulatorio'])]
IC=(TS+TD+NA+CU)/10

riesgos = [
(1,'Riesgo de Datos','Calidad de datos'),
(2,'Riesgo de Datos','Data Poisoning'),
(3,'Riesgo de Datos','Fuga de información'),
(4,'Riesgos del Modelo','Falta de explicabilidad'),
(5,'Riesgos del Modelo','Baja precisión'),
(6,'Riesgos del Modelo','Vulnerabilidad del modelo'),
(7,'Riesgo de Ciberseguridad','Evasión del modelo'),
(8,'Riesgo de Ciberseguridad','Acceso no autorizado'),
(9,'Riesgo de Ciberseguridad','Ataques adversariales (Input Manipulados)'),
(10,'Riesgos Operacionales','Dependencia excesiva de la IA'),
(11,'Riesgos Operacionales','Falta de supervisión humana'),
(12,'Riesgo de Gobernanza','No hay auditoría'),
(13,'Riesgo de Gobernanza','No hay políticas'),
(14,'Riesgo de Gobernanza','No hay control')]


descripciones_riesgos = {

    "Calidad de datos":
    """
    Problemas relacionados con datos incompletos, incorrectos,
    inconsistentes o desactualizados que pueden afectar el
    desempeño y la confiabilidad del sistema de IA.
    """,

    "Data Poisoning":
    """
    Data Poisoning consiste en alterar las fuentes de datos utilizadas
    durante el entrenamiento o el reentrenamiento (eliminando o modificando
    los datos existentes, así como inyectando datos maliciosos) para degradar
    el rendimiento del modelo, sesgar los resultados hacia un resultado
    específico o crear puertas traseras ocultas.
    """,

    "Fuga de información":
    """
    Divulgación accidental o no autorizada de información sensible
    procesada, almacenada o utilizada por el sistema de inteligencia artificial.
    """,

    "Falta de explicabilidad":
    """
    Incapacidad de comprender o justificar cómo el sistema de IA
    genera sus decisiones, recomendaciones o resultados.
    """,

    "Baja precisión":
    """
    Generación recurrente de resultados incorrectos o poco confiables
    que afectan la efectividad y confiabilidad del sistema.
    """,

    "Vulnerabilidad del modelo":
    """
    Debilidades técnicas presentes en el modelo que podrían ser
    explotadas para alterar su comportamiento o afectar su funcionamiento.
    """,

    "Evasión del modelo":
    """
    Manipulación de las entradas con el objetivo de evitar que el sistema
    detecte una amenaza o genere una clasificación correcta.
    """,

    "Acceso no autorizado":
    """
    Acceso indebido a modelos, datos, configuraciones o recursos
    utilizados por el sistema de inteligencia artificial.
    """,

    "Ataques adversariales (Input Manipulados)":
    """
    Entradas manipuladas deliberadamente para engañar al modelo
    y provocar inferencias, clasificaciones o decisiones incorrectas.
    """,

    "Dependencia excesiva de la IA":
    """
    Uso excesivo de los resultados del sistema de IA sin mecanismos
    suficientes de validación o supervisión humana.
    """,

    "Falta de supervisión humana":
    """
    Ausencia de revisión, seguimiento o intervención humana sobre las
    decisiones generadas por el sistema de inteligencia artificial.
    """,

    "No hay auditoría":
    """
    Inexistencia de mecanismos formales para revisar, verificar y evaluar
    el funcionamiento, desempeño y utilización del sistema de IA.
    """,

    "No hay políticas":
    """
    Ausencia de normas, procedimientos o lineamientos organizacionales
    que regulen el uso responsable de la inteligencia artificial.
    """,

    "No hay control":
    """
    Carencia de controles técnicos, operativos o de gobernanza que permitan
    gestionar adecuadamente los riesgos asociados al sistema de IA.
    """
}

st.header('2) Identificación de Riesgos')
seleccionados=[]
for n,c,r in riesgos:
    descripcion = descripciones_riesgos.get(r,"")

    if st.checkbox(
        f'{n}. {r} ({c})',
        help=descripcion
   ):
 
        seleccionados.append(r)

controles_map = {
'Calidad de datos':['Calidad de datos','Procedencia de datos','Validación del Modelo'],
'Data Poisoning':['Calidad de datos','Procedencia de datos','Validación del Modelo','Monitoreo y Registro','Gestión de Incidentes y Auditoría'],
'Fuga de información':['Política IA','Protección de Datos','Monitoreo y Registro','Gestión de Incidentes y Auditoría'],
'Falta de explicabilidad':['Supervisión Humana','Validación del Modelo','Explicabilidad y Transparencia'],
'Baja precisión':['Supervisión Humana','Calidad de datos','Procedencia de datos','Validación del Modelo','Monitoreo y Registro'],
'Vulnerabilidad del modelo':['Protección de Datos','Validación del Modelo','Monitoreo y Registro','Gestión de Incidentes y Auditoría'],
'Evasión del modelo':['Validación del Modelo','Monitoreo y Registro','Gestión de Incidentes y Auditoría'],
'Acceso no autorizado':['Roles y Responsabilidades','Protección de Datos','Monitoreo y Registro','Gestión de Incidentes y Auditoría'],
'Ataques adversariales (Input Manipulados)':['Validación del Modelo','Monitoreo y Registro','Gestión de Incidentes y Auditoría'],
'Dependencia excesiva de la IA':['Política IA','Roles y Responsabilidades','Supervisión Humana','Explicabilidad y Transparencia'],
'Falta de supervisión humana':['Política IA','Roles y Responsabilidades','Supervisión Humana','Gestión de Incidentes y Auditoría'],
'No hay auditoría':['Política IA','Roles y Responsabilidades','Monitoreo y Registro','Gestión de Incidentes y Auditoría'],
'No hay políticas':['Política IA','Roles y Responsabilidades','Gestión de Incidentes y Auditoría'],
'No hay control':['Política IA','Roles y Responsabilidades','Supervisión Humana','Protección de Datos','Validación del Modelo','Monitoreo y Registro','Gestión de Incidentes y Auditoría']}


# Recomendaciones por Riesgo


recomendaciones = {

    "Calidad de datos": [
        "Definir criterios formales de calidad de datos.",
        "Implementar procesos de validación de datos de entrada.",
        "Realizar revisiones periódicas de consistencia e integridad.",
        "Mantener trazabilidad sobre el origen de los datos.",
        "Documentar los procesos de limpieza y preparación de datos."
    ],

    "Data Poisoning": [
        "Validar la procedencia de los datos de entrenamiento.",
        "Aplicar mecanismos de detección de anomalías en los conjuntos de datos.",
        "Restringir el acceso a los repositorios de entrenamiento.",
        "Realizar pruebas periódicas para detectar manipulaciones de datos.",
        "Mantener registros de cambios sobre los datos de entrenamiento."
    ],

    "Fuga de información": [
        "Implementar controles de acceso basados en roles.",
        "Aplicar cifrado a los datos sensibles almacenados y transmitidos.",
        "Monitorear accesos y descargas de información.",
        "Establecer políticas de clasificación y protección de datos.",
        "Definir procedimientos de respuesta ante incidentes de privacidad."
    ],

    "Falta de explicabilidad": [
        "Implementar mecanismos de explicabilidad en los resultados del modelo.",
        "Documentar los criterios utilizados para la toma de decisiones.",
        "Mantener trazabilidad de las predicciones realizadas.",
        "Incorporar validación humana en decisiones críticas.",
        "Capacitar a los usuarios sobre el funcionamiento del sistema."
    ],

    "Baja precisión": [
        "Revisar periódicamente el rendimiento del modelo.",
        "Utilizar conjuntos de datos representativos y actualizados.",
        "Implementar procesos de reentrenamiento del modelo.",
        "Monitorear métricas de desempeño continuamente.",
        "Comparar resultados con referencias o procesos existentes."
    ],

    "Vulnerabilidad del modelo": [
        "Actualizar periódicamente los componentes del modelo.",
        "Aplicar controles de integridad sobre modelos y pesos entrenados.",
        "Restringir modificaciones no autorizadas.",
        "Realizar pruebas de robustez periódicas.",
        "Monitorear comportamientos anómalos del modelo."
    ],

    "Evasión del modelo": [
        "Implementar pruebas con ejemplos adversariales.",
        "Validar las entradas antes de procesarlas.",
        "Monitorear patrones inusuales en las consultas recibidas.",
        "Reentrenar el modelo con ejemplos de evasión detectados.",
        "Mantener un proceso continuo de mejora del modelo."
    ],

    "Acceso no autorizado": [
        "Implementar autenticación multifactor.",
        "Aplicar el principio de mínimo privilegio.",
        "Registrar y monitorear todos los accesos.",
        "Revisar periódicamente cuentas y permisos.",
        "Auditar cambios realizados en datos y modelos."
    ],

    "Ataques adversariales (Input Manipulados)": [
        "Validar y sanitizar las entradas recibidas.",
        "Realizar pruebas de resistencia frente a inputs adversariales.",
        "Monitorear anomalías en las entradas.",
        "Fortalecer la robustez mediante entrenamiento adversarial.",
        "Controlar los canales de entrada de información."
    ],

    "Dependencia excesiva de la IA": [
        "Mantener supervisión humana para decisiones críticas.",
        "Definir cuándo la decisión final corresponde al usuario.",
        "Implementar validaciones manuales.",
        "Capacitar a los usuarios en el uso adecuado de la herramienta.",
        "Evitar automatizar completamente procesos de alto impacto."
    ],

    "Falta de supervisión humana": [
        "Definir responsables para revisar los resultados del sistema.",
        "Establecer puntos de control humano en procesos críticos.",
        "Documentar procedimientos de revisión.",
        "Implementar esquemas de doble validación.",
        "Registrar las decisiones tomadas por los operadores."
    ],

    "No hay auditoría": [
        "Implementar auditorías periódicas sobre el sistema de IA.",
        "Mantener registros completos de eventos.",
        "Documentar cambios realizados al modelo.",
        "Definir indicadores de seguimiento y desempeño.",
        "Realizar revisiones independientes periódicas."
    ],

    "No hay políticas": [
        "Desarrollar una política institucional de IA.",
        "Definir procedimientos para la gestión de riesgos de IA.",
        "Establecer roles y responsabilidades claros.",
        "Formalizar lineamientos de seguridad y gobernanza.",
        "Comunicar las políticas a todos los usuarios."
    ],

    "No hay control": [
        "Implementar controles técnicos y organizacionales.",
        "Establecer mecanismos de monitoreo continuo.",
        "Definir procesos formales."
     ],
    }

st.header('3) Identificación de Controles')
valores_c={}
for riesgo in seleccionados:
    st.subheader(riesgo)
    vals=[]
    for ctrl in controles_map[riesgo]:
        v=st.selectbox(f'{riesgo} - {ctrl}',[1,2,3],key=f'{riesgo}{ctrl}')
        vals.append(v)
    valores_c[riesgo]=sum(vals)/len(vals)
    st.write(f'Índice de Control: {valores_c[riesgo]:.2f}')

st.header('4) Valoración Cuantitativa del Riesgo')
resultados=[]
for riesgo in seleccionados:
    p=st.selectbox(f'Probabilidad - {riesgo}',[1,2,3],key=f'p{riesgo}')
    i=st.selectbox(f'Impacto - {riesgo}',[1,2,3],key=f'i{riesgo}')
    e=st.selectbox(f'Exposición - {riesgo}',[1,2],key=f'e{riesgo}')
    c=valores_c.get(riesgo,1)
    ri=p*i*e
    rr=ri/c
    resultados.append([riesgo,p,i,e,round(c,2),ri,round(rr,2)])

if st.button('Calcular Resultados'):
    if resultados:
        df=pd.DataFrame(resultados,columns=['Riesgo','P','I','E','C','RI','RR'])
        st.dataframe(df,use_container_width=True)
        rit=df['RI'].mean()
        rrf=df['RR'].mean()
        rt=(rrf*0.85)+(IC*2.7)
        nivel='Bajo' if rt<5 else ('Medio' if rt<10 else 'Alto')
        st.header('Resultados')
        st.write('Nombre del Sistema:',nombre)
        st.write('Riesgos Seleccionados:',', '.join(seleccionados))
        st.write(f'Indice Contextual (IC): {IC:.2f}')
        st.write(f'Riesgo Inherente Total: {rit:.2f}')
        st.write(f'Riesgo Residual Total: {rrf:.2f}')
        st.write(f'Riesgo Total (RT): {rt:.2f}')
        
        st.success(f'Nivel de Riesgo: {nivel}')
        
        
        st.header("recomendaciones")

        for riesgo in seleccionados:

            if riesgo in recomendaciones:

               with st.expander(
                  f"Recomendaciones para: {riesgo}"
                 ):

                  for recomendacion in recomendaciones[riesgo]:
                      st.write(f"✅ {recomendacion}") 
    else:
        st.warning('Seleccione al menos un riesgo.')
