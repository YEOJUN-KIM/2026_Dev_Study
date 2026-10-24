import { Link, Navigate, Route, Routes } from "react-router-dom";
import { useSelector } from "react-redux";

import Home from "./pages/Home";
import Board from "./pages/Board";
import BoardWrite from "./pages/BoardWrite";
import BoardContent from "./pages/BoardContent";
import Login from "./pages/Login";
import Join from "./pages/Join";
import Logout from "./pages/Logout";
import MyPage from "./pages/MyPage";
import ItemInsert from "./pages/ItemInsert";
import ItemList from "./pages/ItemList";
import Chat from "./pages/Chat";
import ChangeInfo from "./pages/mypage/ChangeInfo";
import ChangePassword from "./pages/mypage/ChangePassword";
import Footer from "./components/Footer";

import "./css/App.css";

const App = () => {
  const { isLogin } = useSelector((state) => state.logged);

  return (
    <div className="app">
      <nav className="navbar">
        <Link to="/"><button className="nav-button">홈</button></Link>
        <Link to="/board"><button className="nav-button">게시판</button></Link>
        {!isLogin && <Link to="/login"><button className="nav-button">로그인</button></Link>}
        {!isLogin && <Link to="/join"><button className="nav-button">회원가입</button></Link>}
        {isLogin && <Link to="/logout"><button className="nav-button">로그아웃</button></Link>}
        {isLogin && <Link to="/mypage"><button className="nav-button">My페이지</button></Link>}
        {isLogin && <Link to="/item_insert"><button className="nav-button">물품등록</button></Link>}
        {isLogin && <Link to="/item_list"><button className="nav-button">물품</button></Link>}
        <Link to="/chat"><button className="nav-button">채팅</button></Link>
      </nav>

      <main className="main-content">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/board" element={<Board />} />
          <Route path="/board_write" element={<BoardWrite />} />
          <Route path="/board_content" element={<BoardContent />} />
          <Route path="/login" element={<Login />} />
          <Route path="/join" element={<Join />} />
          <Route path="/logout" element={isLogin ? <Logout /> : <Navigate to="/login" />} />
          <Route path="/mypage" element={isLogin ? <MyPage /> : <Navigate to="/login" />}>
            <Route path="change-info" element={<ChangeInfo />} />
            <Route path="change-password" element={<ChangePassword />} />
          </Route>
          <Route path="/item_insert" element={<ItemInsert />} />
          <Route path="/item_list" element={<ItemList />} />
          <Route path="/chat" element={<Chat />} />
        </Routes>
      </main>

      <Footer title="PKNU" />
    </div>
  );
};

export default App;
