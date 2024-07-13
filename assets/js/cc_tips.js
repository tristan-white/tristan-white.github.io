
const imageUrlToBase64 = async (url) => {
    const data = await fetch(url);
    const blob = await data.blob();
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(blob);
        reader.onloadend = () => {
        const base64data = reader.result;
        resolve(base64data);
        };
        reader.onerror = reject;
    });
};



async function genPDF() {
    // Default export is a4 paper, portrait, using millimeters for units
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    const obj = {
        align: 'center' // or any other value you want to assign
    };

    const pageWidth = doc.internal.pageSize.getWidth();
    const pageHeight = doc.internal.pageSize.getHeight();

    var airplaneImg = await imageUrlToBase64('https://images.unsplash.com/photo-1500835556837-99ac94a94552?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');

    // Calculate text dimensions to center it
    // console.log(doc.getFontList());
    doc.setTextColor("#ffffff")
    doc.setFont("calibri", "italic", 500)
    // doc.setFontSize(30)
    const text = "Adventure Awaits."
    const textWidth = doc.getTextWidth(text);
    const textHeight = doc.getFontSize() / doc.internal.scaleFactor;

    const x = (pageWidth - textWidth) / 1.2;
    const y = (pageHeight + textHeight) / 1.2;

    doc.addImage(airplaneImg, 0, 0, pageWidth, pageHeight);
    doc.text(text, x, y);

    doc.addPage()

    var parisImg = await imageUrlToBase64('https://images.unsplash.com/photo-1549144511-f099e773c147?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
    
    doc.addImage(parisImg, 0,0, pageWidth, pageHeight);

    // Draw the white box (filled rectangle)
    doc.setFillColor(255, 255, 255); // Set fill color to white
    doc.rect(10, 10, 180, 50, 'F'); // 'F' means filled

    // Define the text to be added
    const text2 = "This is the first line of text.  This is the second line of text, which should wrap within the box. Here is the third line of text, ensuring that all text is left-justified.";

    // Set the font size
    doc.setFontSize(12);
    doc.setTextColor("#000000")

    // Split the text into lines that fit within the box
    const lines = doc.splitTextToSize(text2, 175);

    // Add the lines of text inside the box
    doc.text(lines, 10 + 2, 10 + 10);

    // doc.beginFormObject(100, 100, pageWidth/2, pageHeight/2)

    doc.output("pdfobjectnewwindow");
    // doc.save("a4.pdf");
}