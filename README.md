# Advanced Programming Language
**Inveninato - Cocuzza**

## Librerie Utilizzate

### Python
- **Flask**: framework per lo sviluppo di applicazioni web.
- **SQLAlchemy**: ORM (Object-Relational Mapping) e toolkit SQL per la gestione di database.

### C#
- **Newtonsoft.Json**: libreria per la gestione e manipolazione di JSON.

### Go
- **Echo**: framework web ad alte prestazioni, facile da utilizzare.

## Installazione

### Python
Per installare i pacchetti richiesti, eseguire il seguente comando utilizzando `pip`:

```bash
pip install -r requirements.txt
```

### C#
Per installare le librerie necessarie tramite NuGet, utilizzare il comando:
```bash
nuget install "nome_libreria"
```

### Go
Per installare Echo, utilizzare il seguente comando:
```bash
go get -u github.com/labstack/echo/v4
```

## Utilizzo
1. **Avviare il Database**: 
- Prima di tutto avviare il database MySQL utilizzando XAMPP o un altro gestore di server MySQL.

2. **Avviare il Server Python**: 
- Eseguire il server Python per gestire l'autenticazione e altre operazioni.

3. **Avviare il Server Go**: 
- Successivamente, avviare il server Go per gestire le richieste API legate alla ricerca e gestione dei preferiti.

4. **Avviare il client C#**:
- Una volta che entrambi i server sono in esecuzione, avviare il client C# per iniziare a utilizzare l'applicazione.

### Funzionalità dell'Applicazione
- Registrazione e Login: All'avvio del client, l'utente può registrarsi o loggarsi nel sistema.
- Ricerca Voli: Gli utenti possono cercare voli e visualizzare le opzioni disponibili.
- Gestione Preferiti: Gli utenti possono salvare i voli nei preferiti per ricevere notifiche su eventuali cambiamenti di prezzo.

