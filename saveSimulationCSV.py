import csv
    
def save_simulation_results_to_csv(metrics, filename="simulation_resultsSummary.csv"):
    """Saves simulation metrics to a CSV file."""
    
    # Validate data structure
    if not isinstance(metrics, dict):
        print("ERROR: Metrics is not a dictionary.")
        return
    
    if 'production' not in metrics:
        print("ERROR: 'production' key missing in metrics.")
        return
    
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Metric", "Value"])

            # Save production metrics
            writer.writerow(["Average Total Production", metrics['production']['avg_total']])
            writer.writerow(["Production Standard Deviation", metrics['production']['std_total']])
            writer.writerow(["Average Faulty Products", metrics['production']['avg_faulty']])
            writer.writerow(["Average Faulty Rate", metrics['production']['avg_faulty_rate']])

            # Save station metrics
            for i in range(6):
                writer.writerow([f"Station {i+1} Occupancy Rate", metrics['station_metrics']['avg_occupancy_rates'][i]])
                writer.writerow([f"Station {i+1} Average Wait Time", metrics['station_metrics']['avg_wait_times'][i]])
                writer.writerow([f"Station {i+1} Downtime", metrics['station_metrics']['avg_downtimes'][i]])

            # Save time metrics
            writer.writerow(["Average Production Time", metrics['time_metrics']['avg_production_time']])
            writer.writerow(["Average Fixing Time", metrics['time_metrics']['avg_fixing_time']])
            writer.writerow(["Average Supplier Occupancy", metrics['time_metrics']['avg_supplier_occupancy']])
        
        print(f"✅ Simulation results saved to {filename}")

    except Exception as e:
        print("ERROR writing to CSV:", e)

def save_single_run_metrics_to_csv(metrics, filename="single_run_results.csv"):
    """Saves a single simulation run's metrics to a CSV file."""
    
    # Convert JSON string to dictionary if needed
    if isinstance(metrics, str):
        try:
            metrics = json.loads(metrics)
        except json.JSONDecodeError:
            print("ERROR: Invalid JSON format for metrics.")
            return

    # Validate data structure
    if not isinstance(metrics, dict):
        print("ERROR: Metrics is not a dictionary.")
        return
    
    if 'production' not in metrics or 'station_metrics' not in metrics or 'time_metrics' not in metrics:
        print("ERROR: Missing expected keys in metrics.")
        return

    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Metric", "Value"])

            # Save production metrics
            writer.writerow(["Total Production", metrics['production']['total']])
            writer.writerow(["Faulty Products", metrics['production']['faulty']])
            writer.writerow(["Faulty Rate", metrics['production']['faulty_rate']])

            # Save station metrics
            for i in range(6):
                writer.writerow([f"Station {i+1} Occupancy Rate", metrics['station_metrics']['occupancy_rates'][i]])
                writer.writerow([f"Station {i+1} Wait Time", metrics['station_metrics']['wait_times'][i]])
                writer.writerow([f"Station {i+1} Downtime", metrics['station_metrics']['downtimes'][i]])

            # Save time metrics
            writer.writerow(["Production Time", metrics['time_metrics']['avg_production_time']])
            writer.writerow(["Fixing Time", metrics['time_metrics']['avg_fixing_time']])
            writer.writerow(["Supplier Occupancy", metrics['time_metrics']['supplier_occupancy']])
        
        print(f"✅ Single run results saved to {filename}")

    except Exception as e:
        print("ERROR writing to CSV:", e)