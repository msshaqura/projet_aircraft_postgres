"""
Package src pour l'analyse des données d'aviation
"""

from .database import get_connection, execute_query

__all__ = ['get_connection', 'execute_query']