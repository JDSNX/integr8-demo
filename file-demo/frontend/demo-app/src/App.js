import React, { useState } from "react"
import './App.css';
import api from './hooks/api'
import Pagination from 'react-js-pagination';


const App = () => {  
  const [status, setStatus] = useState('Not started');
  const [summaries, setSummaries] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [itemsPerPage] = useState(10);

  const handleETL = async () => {
    try {
      setStatus('In progress');
      const response = await api.post('/api/etl');
      setStatus('Completed');
      setSummaries(response.data);
    } catch (error) {
      setStatus('Failed');
      console.error('ETL process failed:', error.message);
    }
  };

  const handlePageChange = (pageNumber) => setCurrentPage(pageNumber);

  const getStatusColor = (status) => {
    switch (status) {
      case 'In progress':
        return 'yellow';
      case 'Completed':
        return 'green';
      case 'Failed':
      case 'Not started':
      default:
        return 'red';
    }
  };

  
  return (
    <div className="app-container">
      <div className="background-gradient"></div>
      <div className="content-container">
        <button onClick={handleETL}>Trigger ETL</button>
        <p style={{ color: getStatusColor(status) }}>Status: {status}</p>
        {status === 'Completed' && (
          <div>
            <h2>Summaries:</h2>
            <table>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Title</th>
                  <th>Summary</th>
                </tr>
              </thead>
              <tbody>
                {summaries
                  .slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage)
                  .map((post, index) => (
                    <tr key={index}>
                      <td>{post.id}</td>
                      <td>{post.title}</td>
                      <td>{post.summary}</td>
                    </tr>
                  ))}
              </tbody>
            </table>
            <Pagination
              activePage={currentPage}
              itemsCountPerPage={itemsPerPage}
              totalItemsCount={summaries.length}
              pageRangeDisplayed={10}
              onChange={handlePageChange}
              itemClass="page-item"
              linkClass="page-link"
            />
          </div>
        )}
      </div>
    </div>

  );
}

export default App;
