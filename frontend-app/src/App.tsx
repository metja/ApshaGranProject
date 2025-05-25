import {useEffect, useState } from 'react'
import axios from 'axios'
import './App.css'


function DataFetcher() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    axios.get('http://0.0.0.0:8000/categories/') // 🔁 заміни на свій ендпоінт
      .then(response => {
        setData(response.data);
        setLoading(false);
      })
      .catch(error => {
        setError('Помилка при завантаженні');
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Завантаження...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div>
      <h3>Отримані дані:</h3>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default DataFetcher;
