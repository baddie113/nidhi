def shutdown() -> str:
    response = input("Do you want to shut down? (yes/no): ")
    match response:
        case "yes":
            return "shutting down"
def main():       
        result = shutdown() 
        if result == "shutting down":
          print("System is shutting down...")
if __name__ == "__main__":
    main()