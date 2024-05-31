const CodeComponent = () => {

    const handleClick = () => {
        console.log('You have clicked Code');
    }
    return (  
       <div className="codeBar">

        <button className="Code" onClick={handleClick}> Learn with Coding with our AI tutor</button>

       </div>
    );
}
 
export default CodeComponent;