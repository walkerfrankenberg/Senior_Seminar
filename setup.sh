mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[theme]\n\
primaryColor=\"#1D84B5\"\n\
backgroundColor=\"#EBEBEB\"\n\
secondaryBackgroundColor=\"#0A2239\"\n\
textColor=\"#0F3457\"\n\
font=\"sans serif\"\n\
\n\
" > ~/.streamlit/config.toml