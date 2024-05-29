const Document = () => {

    const handleClick = () => {
        console.log('You have clicked Doc');
    }   
    return ( 
        <div className="docBar">
        

        <button className="Doc" onClick={handleClick}> Click To talk with your Document</button>
            
        </div>
     );
}
 
export default Document;