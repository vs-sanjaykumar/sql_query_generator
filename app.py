import streamlit as st
import google.generativeai as genai
GOOGLE_API_KEY="AIzaSyBwPmE8nCWi9sw_WopPA6RYHVLoWmnj_Lk"

genai.configure(api_key=GOOGLE_API_KEY)
model=genai.GenerativeModel('gemini-pro')
def main():
    st.set_page_config(page_title="SQL QUERY GENERATOR",page_icon=":robot:")
    st.markdown(
        """
             <div style="text-align : center;">
                <h1>SQL QUERY GENERATOR</h1>
                <h3> I can generate SQL queries to you</h3>
                <h4> It give Explanation as well!!!</h4>
                <P> Based on the prompt given , it give queries</p>
            </div>
        """,
        unsafe_allow_html=True,
    )

    text_input=st.text_area("Enter the Query in plain english text")

    
    submit=st.button("Generate SQL Query")

    if submit:
        with st.spinner("Generating SQL query ..."):
            template="""
                            Create a SQL Query snippet using the below text:
                     ```
                        {text_input}
                     ```
                    I just want a SQL Query
                     
                    """
            formatted_template=template.format(text_input=text_input)
                    
            st.write(formatted_template)
            response=model.generate_content(formatted_template)
            sql_query=response.text

            sql_query=sql_query.strip().lstrip("```sql").rstrip("```")
            


            expected_output="""
                    What would be the expected response of this SQL query snippet :             
                    ```     
                    {sql_query}
                    ```
                    provide sample tabular response with no explanation
                     
                    """
            eof=expected_output.format(sql_query=sql_query)
            eout=model.generate_content(eof)        
            eout=eout.text
            

            explain="""
                    Explain this SQL Query:
                    ```
                        {sql_query}

                    ```
                    please provide with simplest of explanation:

            """
            explanation_formatted=explain.format(sql_query=sql_query)
            explain=model.generate_content(explanation_formatted)
            explain=explain.text
            
            with st.container():
                st.success("SQL Query Generated Successfully! Here is your Query Below :")
                st.code(sql_query,language="sql")

                st.success("Expected  output of the SQL Query will be :")
                st.markdown(eout)

                st.success("Explanation of the SQL Query:")
                st.markdown(explain)

main()