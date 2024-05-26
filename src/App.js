import Home from './Home';
import Navbar from './Navbar';
import CodeComponent from './CodeComponent';
import ProfComponent from './ProfComponent';
import Document from './Document';

function App() {
  return (
    <div className="App">

      <Navbar />
      <div className="content">
        
        <Home />
        
      </div>
      <div className="pathways">
        
        <CodeComponent />
        <ProfComponent />
        <Document />

      </div>


      
    </div>
  );
}

export default App;
