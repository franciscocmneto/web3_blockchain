import Pages from "./Pages/Pages";
import Category from "./Components/Category";
import { BrowserRouter } from "react-router-dom";
import Search from "./Components/Search";
import { styled } from "styled-components";

function App() {
  return (

    <BrowserRouter>
      <div className="App">
        <Search/>
        <Category />
        <Pages />

        
      </div>
    </BrowserRouter>
  );
}

export default App;
