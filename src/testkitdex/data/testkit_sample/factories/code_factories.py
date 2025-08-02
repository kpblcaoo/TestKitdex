"""
Code Factories for generating C# code strings
"""

from factory import Factory, Faker
from typing import Dict, Any


class CSharpCodeFactory(Factory):
    """Factory for creating C# code strings"""
    
    class Meta:
        model = str
    
    @classmethod
    def create_user_factory_code(cls) -> str:
        """Создать код метода фабрики пользователя"""
        return '''
        /// <summary>
        /// Creates a test user
        /// </summary>
        /// <param name="name">User name</param>
        /// <returns>User object</returns>
        /// <tags>user, factory, test-data</tags>
        public static User CreateUser(string name = "TestUser")
        {
            return new User { Name = name };
        }
        '''
    
    @classmethod
    def create_message_factory_code(cls) -> str:
        """Создать код метода фабрики сообщения"""
        return '''
        /// <summary>
        /// Creates a test message
        /// </summary>
        /// <param name="text">Message text</param>
        /// <returns>Message object</returns>
        /// <tags>message, factory, telegram</tags>
        public static Message CreateMessage(string text = "Test message")
        {
            return new Message { Text = text };
        }
        '''
    
    @classmethod
    def create_generic_factory_code(cls) -> str:
        """Создать код generic метода фабрики"""
        return '''
        /// <summary>
        /// Generic factory method
        /// </summary>
        /// <typeparam name="T">Type to create</typeparam>
        /// <returns>Created object</returns>
        /// <tags>factory, generic</tags>
        public static T CreateFactory<T>() where T : new()
        {
            return new T();
        }
        '''
    
    @classmethod
    def create_simple_method_code(cls) -> str:
        """Создать код простого метода без тегов"""
        return '''
        public void DoSomething()
        {
            // Simple method without tags
            Console.WriteLine("Hello World");
        }
        '''
    
    @classmethod
    def create_testkit_class_code(cls) -> str:
        """Создать код класса TestKit с несколькими методами"""
        return '''
        public class TestKit
        {
            /// <summary>
            /// Creates a test user
            /// </summary>
            /// <param name="name">User name</param>
            /// <returns>User object</returns>
            /// <tags>user, factory, test-data</tags>
            public static User CreateUser(string name = "TestUser")
            {
                return new User { Name = name };
            }
            
            /// <summary>
            /// Creates a test message
            /// </summary>
            /// <param name="text">Message text</param>
            /// <returns>Message object</returns>
            /// <tags>message, factory, telegram</tags>
            public static Message CreateMessage(string text = "Test message")
            {
                return new Message { Text = text };
            }
            
            /// <summary>
            /// Generic factory method
            /// </summary>
            /// <typeparam name="T">Type to create</typeparam>
            /// <returns>Created object</returns>
            /// <tags>factory, generic</tags>
            public static T CreateFactory<T>() where T : new()
            {
                return new T();
            }
        }
        '''
    
    @classmethod
    def create_complex_method_code(cls) -> str:
        """Создать код сложного метода с параметрами"""
        return '''
        /// <summary>
        /// Processes data with multiple parameters
        /// </summary>
        /// <param name="id">Data ID</param>
        /// <param name="name">Data name</param>
        /// <param name="active">Active status</param>
        /// <returns>Processed result</returns>
        /// <tags>processing, data</tags>
        public string ProcessData(int id, string name, bool active = true)
        {
            if (!active)
                return "Inactive";
                
            return $"Processed: {id} - {name}";
        }
        '''


# Удобные функции для обратной совместимости
def create_user_factory_code() -> str:
    """Создать код метода фабрики пользователя (совместимость)"""
    return CSharpCodeFactory.create_user_factory_code()

def create_message_factory_code() -> str:
    """Создать код метода фабрики сообщения (совместимость)"""
    return CSharpCodeFactory.create_message_factory_code()

def create_generic_factory_code() -> str:
    """Создать код generic метода фабрики (совместимость)"""
    return CSharpCodeFactory.create_generic_factory_code()

def create_simple_method_code() -> str:
    """Создать код простого метода (совместимость)"""
    return CSharpCodeFactory.create_simple_method_code()

def create_testkit_class_code() -> str:
    """Создать код класса TestKit (совместимость)"""
    return CSharpCodeFactory.create_testkit_class_code() 