## Deploy to int server

### Vault password file
Export the path to the ansible-vault password file for easy usage of the vault files

```bash
export ANSIBLE_VAULT_PASSWORD_FILE=<whatever the location of your password file is>
```

### Inventory
The hosts are divided into 2 groups: ``testing`` (uat) and ``prod``. The testing servers are under the group ``grp-testing``
and the prod servers are under the group ``grp-prod``. There are two inventory files: ``jick-inventory-local`` (works inside
JICK's internal network ) and ``jick-inventory-prod`` (works both inside and outside JICK's internal network ).

### Deploy inside JICK's network

It uses the **jick-inventory-local** inventory file

```bash
ansible-playbook -f1 -i jick-inventory-local -vvvv -ttesting-int -ltesting-int jick-testing.yml --private-key ~/.ssh/google_compute_engine
```

### Deploy SOLR to the `prod-mq` server
```bash
ansible-playbook -i jick-inventory-local jick-solr.yml --ask-vault-password
```


### Deploy while outside JICK's network

It uses the **jick-inventory-remote** inventory file

```bash
ansible-playbook -f1 -i jick-inventory-remote -vvvv -ttesting-int -ltesting-int jick-testing.yml --private-key ~/.ssh/google_compute_engine
```
### Deploy the tasks only
```bash
ansible-playbook -vvv -i jick-inventory-local --tags='integration_service_tasks' -l prod-app jick-prod.yml
```
