## Solutions Considered  

1. Reading the Entire Log File into Memory  
   - Pros: Simple to implement.  
   - Cons: Inefficient for large files, high memory usage.  

2. Streaming Log File Line-by-Line  
   - Pros: Memory-efficient, scalable for large files.  
   - Cons: Slightly more complex implementation.  

3. Using External Tools (e.g., `grep`)  
   - Pros: Very fast for filtering text.  
   - Cons: Less control over processing, OS-dependent.  

---

## Final Solution Summary  

We chose the line-by-line streaming approach because it provides an optimal balance of performance and memory efficiency. This ensures the script can handle large log files without excessive RAM usage. The extracted logs are stored in an organized structure under the `output/` directory, making retrieval straightforward.  

---

## Steps to Run  

1. Ensure Python 3.x is installed. 
2. Download the logs file from given url in Readme.md.
3. Extract the logs file from the zip to the route directory of the project. 
4. Navigate to the `src` directory in your terminal.  
5. Run the script using:  
   ```sh
   python extract_logs.py YYYY-MM-DD
   ```  
   Replace `YYYY-MM-DD` with the target date.  
6. The filtered log entries will be saved in:  
   ```
   output/output_YYYY-MM-DD.txt
   ```  
