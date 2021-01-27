def infoclientesum(base,carac):
   return base.groupby(carac)['CLIENTNUM'].count()
