""" 
1. Add a new class inheriting from User called FrenchUser and when greeting, it should say “Bonjour - Name”
2. Add a new class inheriting from User called SpanishUser and when greeting, it should say “Hola! - Name”
3. Test both classes
4. Move each class into their files
"""

from french_user import FrenchUser
from spanish_user import SpanishUser

manon = FrenchUser("Manon")
manon.greet()

carolina = SpanishUser("Carolina")
carolina.greet()