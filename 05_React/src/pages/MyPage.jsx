import React from 'react';
import { Link, Outlet } from 'react-router-dom';

const MyPage = () => {
    return (
        <div>
            <Link to={"/mypage/change-password"}><button>암호변경</button> </Link>
            
            <Link to={"/mypage/change-info"}><button>정보변경</button> </Link>
            <Outlet />
        </div>
    );
};

export default MyPage;
