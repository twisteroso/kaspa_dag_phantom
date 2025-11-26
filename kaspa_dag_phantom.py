import requests, time

def dag_phantom():
    print("Kaspa — The DAG Phantom Just Passed Through the Mesh")
    seen = set()
    while True:
        r = requests.get("https://api.kaspa.org/transactions/recent")
        for tx in r.json().get("transactions", []):
            txid = tx["transactionId"]
            if txid in seen: continue
            seen.add(txid)

            mass = tx.get("mass", 0)
            value = sum(out["value"] for out in tx.get("outputs", [])) / 1e8
            
            if mass > 1_000_000 and value > 100_000:  # >100k KAS + insane mass
                print(f"THE PHANTOM TRAVERSED THE DAG\n"
                      f"{value:,.0f} KAS just moved at light speed\n"
                      f"Mass: {mass:,} — denser than neutron star\n"
                      f"Inputs: {len(tx['inputs'])}\n"
                      f"Outputs: {len(tx['outputs'])}\n"
                      f"Tx: https://explorer.kaspa.org/txs/{txid}\n"
                      f"→ This transaction exists in multiple blocks simultaneously\n"
                      f"→ Kaspa didn't confirm it. Kaspa inhaled it.\n"
                      f"→ The DAG itself blinked.\n"
                      f"{'◈◈◈'*30}\n")
        time.sleep(0.4)  # Kaspa is scary fast

if __name__ == "__main__":
    dag_phantom()
