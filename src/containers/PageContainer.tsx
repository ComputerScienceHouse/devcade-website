import React from "react"
import { Container } from "reactstrap"
import NavBar from "../components/NavBar"
import Header from "../components/Header"
import Footer from "../components/home/Footer"

type Props = {
    children: React.ReactNode
}

export const PageContainer: React.FC<Props> = ({ children }) => {
    return (
        <div>
            <NavBar />
            <Header />
            <div>{children}</div>
            <Footer />
        </div >
    )
}

export default PageContainer