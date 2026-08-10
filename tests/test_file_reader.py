import pytest
from unittest.mock import patch, mock_open
import pandas as pd
from src.file_reader import read_csv_file, read_excel_file


class TestFileReader:
    """Тесты для модуля чтения файлов"""

    @patch('pandas.read_csv')
    def test_read_csv_file_success(self, mock_read_csv):
        """Тест успешного чтения CSV файла"""
        # Мокаем данные
        mock_data = pd.DataFrame([
            {'id': 1, 'amount': 100, 'description': 'Test 1'},
            {'id': 2, 'amount': 200, 'description': 'Test 2'}
        ])
        mock_read_csv.return_value = mock_data

        # Вызываем функцию
        result = read_csv_file('test.csv')

        # Проверяем результат
        assert len(result) == 2
        assert result[0]['id'] == 1
        assert result[1]['amount'] == 200
        mock_read_csv.assert_called_once_with('test.csv', delimiter=";")

    @patch('pandas.read_csv')
    def test_read_csv_file_empty(self, mock_read_csv):
        """Тест чтения пустого CSV файла"""
        mock_read_csv.side_effect = pd.errors.EmptyDataError

        result = read_csv_file('empty.csv')

        assert result == []

    @patch('pandas.read_csv')
    def test_read_csv_file_not_found(self, mock_read_csv):
        """Тест чтения несуществующего CSV файла"""
        mock_read_csv.side_effect = FileNotFoundError

        result = read_csv_file('nonexistent.csv')

        assert result == []

    @patch('pandas.read_excel')
    def test_read_excel_file_success(self, mock_read_excel):
        """Тест успешного чтения Excel файла"""
        # Мокаем данные
        mock_data = pd.DataFrame([
            {'id': 1, 'amount': 150, 'description': 'Excel Test 1'},
            {'id': 2, 'amount': 250, 'description': 'Excel Test 2'}
        ])
        mock_read_excel.return_value = mock_data

        # Вызываем функцию
        result = read_excel_file('test.xlsx')

        # Проверяем результат
        assert len(result) == 2
        assert result[0]['description'] == 'Excel Test 1'
        assert result[1]['amount'] == 250
        mock_read_excel.assert_called_once_with('test.xlsx')

    @patch('pandas.read_excel')
    def test_read_excel_file_empty(self, mock_read_excel):
        """Тест чтения пустого Excel файла"""
        mock_read_excel.side_effect = pd.errors.EmptyDataError

        result = read_excel_file('empty.xlsx')

        assert result == []