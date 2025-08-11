import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register"; // <-- ADD THIS IMPORT
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<Register />} />  {/* <-- ADD THIS LINE */}
    </Routes>
  );
}
export default App;