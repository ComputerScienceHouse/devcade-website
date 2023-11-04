import React from 'react'
import {
    Collapse,
    Container,
    Nav,
    Navbar,
    NavbarToggler,
    NavItem,
} from 'reactstrap'
import { NavLink } from 'react-router-dom'
import Profile from './Profile'
import '../css/navbar.css'

const NavBar: React.FunctionComponent = () => {
    const [isOpen, setIsOpen] = React.useState<boolean>(false)

    const toggle = () => {
        setIsOpen(!isOpen)
    }

    return (
        <div>
            <Navbar id='navbar' dark expand='lg' fixed='top'>
                <Container>
                    <NavLink to='/' className={'navbar-devcade'}>
                        Devcade
                    </NavLink>
                    <NavbarToggler onClick={toggle} />
                    <Collapse isOpen={isOpen} navbar>
                        <Nav navbar>

                            <NavItem>
                                <NavLink to='/' className='nav-link'>
                                    Home
                                </NavLink>
                            </NavItem>

                            <NavItem>
                                <NavLink to='/catalog' className='nav-link'>
                                    Games
                                </NavLink>
                            </NavItem>

                            <NavItem>
                                <NavLink to='/docs#/' className='nav-link'>
                                    Docs
                                </NavLink>
                            </NavItem>

                            <NavItem>
                                <NavLink to='/create_game' className='nav-link'>
                                    Create Game
                                </NavLink>
                            </NavItem>
                        </Nav>
                        <Nav navbar className='ml-auto'>
                            <Profile />
                        </Nav>
                    </Collapse>
                </Container>
            </Navbar>
        </div>
    )
}

export default NavBar