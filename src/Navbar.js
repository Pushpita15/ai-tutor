const Navbar = () => {
    return ( 
        <nav className="navbar">
            <h1>Your Personalized Tutor</h1>
            <div className="links">
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/tutor" style={{
                    color: 'white',
                    backgroundColor: '#f1356d',
                    borderRadius: '9px'
                
                }}>Tutor</a>
            </div>
        </nav>
     );
}
 
export default Navbar;