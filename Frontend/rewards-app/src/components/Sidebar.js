import React from 'react'
import './Sidebar.css';
import { Link } from 'react-router-dom';
import { SidebarRef } from './SidebarRef';

function Sidebar() {
    return (
        <>
            <ul className="sidebar">
                <div className='sidebar-top'>
                    {SidebarRef.filter(item => !item.isBottom).map((item, index) => {
                        return (
                            <li key={index} className={item.className}>
                                <Link to={item.path}>
                                    <img src={item.icon} alt={item.name} className="sidebar-icon" />
                                </Link>
                            </li>
                        )
                    })}
                </div>
                <div className='sidebar-bottom'>
                    {SidebarRef.filter(item => item.isBottom).map((item, index) => {
                        return (
                            <li key={index} className={item.className}>
                                <Link to={item.path}>
                                    <img src={item.icon} alt={item.name} className="sidebar-icon" />
                                </Link>
                            </li>
                        )
                    })}
                </div>
            </ul>
        </>
    )
}

export default Sidebar
