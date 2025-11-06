from app.seeds.seed_commerce import seed_commerces
from app.seeds.seed_terminal import seed_terminals
from app.seeds.seed_contract import seed_contracts
from app.seeds.seed_invoice import seed_invoices
from app.seeds.seed_incident import seed_incidents
from app.seeds.seed_lead import seed_leads
from app.seeds.seed_settlement import seed_settlements
from app.seeds.seed_novelty import seed_novedades
from app.seeds.seed_transaction import seed_transaction_summaries
from app.seeds.seed_support_tickets import seed_support_tickets

def run_all_seeds():
    seed_commerces()
    seed_terminals()
    seed_contracts()
    seed_transaction_summaries()
    seed_leads()
    seed_incidents()
    seed_invoices()
    seed_settlements()
    seed_novedades()
    seed_support_tickets()
