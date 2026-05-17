import json
import numpy as np 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ChatBotCroptops:

    """
    Chatbot inteligente para vender croptops de NAVARROTEX
    """
    def __init__(self, intents_file='intents.json'):
            """
            se ejecuta cuando creas: bot = ChatBotCroptops()
            """
            
            # Abrir y leer archivo JSON
            
            with open(intents_file, 'r', encoding='utf-8') as f:
                self.intents_data = json.load(f)
                
            # Creación de listas vacias para guardar datos
            
            self.patterns = [] # preguntas del entrenamiento
            self.tags = [] # categorias de las preguntas
            self.responses_by_tag = {} # respuestas de tag
            
            # Recorrer cada intent
            
            for intent in self.intents_data['intents']:
                tag = intent['tag'] # precio, colo, saludos, etc.
                
                # para cada pregunta en este intent
                
                for pattern in intent['patterns']:
                    self.patterns.append(pattern.lower()) #minusculas
                    self.tags.append(tag) #categoria
                    
                # guarda las respuestas posibles para este tag
                
                self.responses_by_tag[tag] = intent['responses']
                
            # patrones a números
            
            self.vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(2, 3))
            self.pattern_vectors = self.vectorizer.fit_transform(self.patterns)
            print(f"✅ ChatBot NAVARROTEX listo! Aprendió {len(self.patterns)} patrones")
            
    def reconocer_intento(self, texto_usuario):
        
        """
        Recibe la pregunta del usuario
        Retorna: (intent_encontrado, similitud)
        """
    
        # De pregunta a numeros
    
        vector_usuario = self.vectorizer.transform([texto_usuario.lower()])
    
        # Comparar
    
        similitudes = cosine_similarity(vector_usuario, self.pattern_vectors)[0]
    
        # Encontrar el patron mas parecido
    
        idx_mejor = np.argmax(similitudes) # Indice del numero mas alto
        puntuacion = similitudes[idx_mejor] # El valor de ese numero
    
        # si es muy baja no se entiende
    
        if puntuacion < 0.4:
            return None, puntuacion
    
        # Retorna la categoria del patron mas parecido
    
        categoria = self.tags[idx_mejor]
        return categoria, puntuacion

    def obtener_respuesta(self, texto_usuario):
        
        """
        Recibe pregunta del usuario
        Retorna: (respuesta_texto, intent_identificado)
        """
        
        # Reconocer el intent

        categoria, confianza = self.reconocer_intento(texto_usuario)
        
        # Si no se entiende

        if categoria is None:
            return "Lo siento, no entendí tu pregunta 😅. ¿Puedes explicarme mejor? Pregunta sobre: precios, colores, envíos, talles, etc.", "desconocido"
        
        # Si se entiende, elegir una respuesta aleatoria

        respuestas_posibles = self.responses_by_tag[categoria]
        respuesta_elegida = np.random.choice(respuestas_posibles)
        
        return respuesta_elegida, categoria

if __name__ == "__main__":
    
    bot = ChatBotCroptops()
    
    # Pruebas

    preguntas = [
        "Hola",
        "¿Cuánto cuesta?",
        "¿Qué colores tienen?"
    ]
    
    for pregunta in preguntas:
        
        respuesta, intent = bot.obtener_respuesta(pregunta)
        print(f"👤 {pregunta}")
        print(f"🤖 {respuesta}\n")
