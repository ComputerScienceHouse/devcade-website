import React from "react"
import { Container } from "reactstrap"
import NavBar from "../components/NavBar"
import Header from "../components/Header"

type Props = {
    children: React.ReactNode
}

export const PageContainer: React.FC<Props> = ({ children }) => {
    return (
        <div>
            <NavBar />
            <Header />
            <div>{children}</div>
        </div >
    )
}

export default PageContainer