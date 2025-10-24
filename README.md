<h1 style="color: cyan">PDFChat</h1>

<p><strong>PDFChat</strong> is a Streamlit-based AI chatbot that allows you to upload multiple PDF files and ask questions about their content. 
It uses LangChain, HuggingFace embeddings, and OpenAI models to process, embed, and retrieve answers from your documents.</p>

<h2>Features</h2>
<ul>
    <li>Upload one or more PDF files.</li>
    <li>Extracts text from PDFs and splits it into chunks.</li>
    <li>Embeds the text using HuggingFace sentence-transformers.</li>
    <li>Creates a conversational AI that answers your questions based on the uploaded PDFs.</li>
    <li>Supports conversation memory to keep chat context.</li>
</ul>

<h2>Installation</h2>
<p>Make sure you have Python 3.10+ installed. Then install the required packages:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h2>Usage</h2>
<ol>
    <li>Clone the repository: <code>git clone &lt;repo-url&gt;</code></li>
    <li>Navigate to the project folder: <code>cd PDFChat</code></li>
    <li>Create a <code>.env</code> file and add your <code>API_KEY</code> for OpenAI or OpenRouter.</li>
    <li>Run the app: <code>streamlit run app.py</code></li>
    <li>Upload PDFs and start chatting!</li>
</ol>

<h2>Example</h2>
<p>Upload a PDF about "Eminem" and one about "Morocco", then ask questions like:</p>
<ul>
    <li>"What is this PDF about?"</li>
    <li>"Tell me about Morocco's capital."</li>
    <li>"Who won an Academy Award for 'Lose Yourself'?"</li>
</ul>

<h2>Requirements</h2>
<ul>
    <li>streamlit</li>
    <li>langchain</li>
    <li>PyPDF2</li>
    <li>faiss-cpu</li>
    <li>sentence-transformers</li>
    <li>fpdf (optional, for creating PDFs)</li>
    <li>dotenv</li>
</ul>

<h2>License</h2>
<p>MIT License. Feel free to use and modify!</p>

</body>
</html>
