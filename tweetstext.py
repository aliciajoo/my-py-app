def get_messages(self, msl):
    return self.api.statuses_lookup(msl, include_entities=True)

for 10_batch in batchlist:
	sleep(api.sleepy_time('messages'))
	msgl = api.get_messages(100_batch)
	for message in msgl:
        print message
