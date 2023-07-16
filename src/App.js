import Pages from "./Pages/Pages";
import Category from "./Components/Category";
import { BrowserRouter, NavLink } from "react-router-dom";

function App() {
  return (

    <BrowserRouter>
      <div className="App">
        <Category />
        <Pages />
      </div>
    </BrowserRouter>
  );
}



export default App;
