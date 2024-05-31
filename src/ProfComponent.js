const ProfComponent = () => {

    const handleClick = () => {
        console.log('You have clicked Prof');
    }
    return ( 
        <div className="profBar">
            <button className="Profs" onClick={handleClick}> Click to Leearn any Course with our AI tutor  </button>
        </div>
     );
}
 
export default ProfComponent;