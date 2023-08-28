# In der Theorie haben Sie gelernt, wie mit der Methode isinstance die
# Zugehörigkeit eines Objekts zu einer Klasse festgestellt werden kann
# und wie mit dem Operator is geprüft wird, ob Referenzen identisch sind.
# Der folgende Code geht noch ein bisschen weiter. Sie sollen den Code
# studieren und sein Verhalten erklären. Dazu kann es notwendig sein,
# dass Sie sich über passende Suchbegriffe im Internet "schlau" machen.
class ObjectIdentity:

    def __init__(self, value):
        """
        Erzeugt ein Objekt mit dem Wert des Parameters value
        :param value: ein beliebiger Text
        """
        self._text = value

    @property
    def text(self):
        """
        Liefert den Wert des Attributs
        :return: aktueller Text
        """
        return self._text

    @text.setter
    def text(self, value):
        """
        Schreibt den Wert von value ins Attribut.
        :param value: ein beliebiger Text
        """
        self._text = value

    def __eq__(self, other):
        '''
        Vergleicht zwei Objekte auf deren Inhalt, sodass sie mit dem
        ==-Operator verglichen werden können.
        Diese Methode ist implizit für jedes Objekt verfügbar und kann überschrieben
        werden, um den gewünschten Effekt des Vergleichs zu bekommen.

        Wenn Ihnen nicht klar ist, wie man das macht, suchen Sie im Internet nach Lösungen,
        z.B. diese hier -> https://www.pythontutorial.net/python-oop/python-__eq__/.
        '''
        if isinstance(other, ObjectIdentity):
            return self.text == other.text
        elif isinstance(other, str):
            return self.text == other
        return False


if __name__ == "__main__":
    # erzeugen Sie hier 2 Objekt obj1 und obj2 der Klasse ObjectIdentity.
    # do it
    obj1 = ObjectIdentity('auf ein Wort')
    obj2 = ObjectIdentity('auf ein Wort')

    ##
    # prüfen der Klassenzugehörigkeit von obj1 zur Klasse ObjectIdentity
    # Geben Sie je nach Testergebnis einen passenden Text aus.
    # do it
    if isinstance(obj1, ObjectIdentity):
        print('obj1 ist vom Typ ObjectIdentity')
    else:
        print('obj1 ist nicht vom Typ ObjectIdentity')

    ##
    # prüfen Sie, ob die beiden Objekte obj1 und obj2 identisch sind.
    # Geben Sie je nacht Testergebnis einen passenden Text aus.
    # do it
    if obj1 is obj2:
        print('ob1 und obj2 sind identisch')
    else:
        print('obj1 und obj2 sind nicht identisch')

    ##
    # prüfen Sie hier den Inhalt (das Attribut) der beiden Objekte auf Gleichheit.
    # Beachten Sie dazu auch die Hinweise in der Methode __eq__
    # do it
    if obj1 == obj2:
        print('obj1 und obj2 haben den gleichen Inhalt')
    else:
        print('obj1 und obj2 haben unterschiedlichen Inhalt')