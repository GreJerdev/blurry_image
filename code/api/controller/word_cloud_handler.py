import api.services.word_cloud_service as word_cloud_service
import io
from sanic.response import stream

async def generate_image(request):
    try:

        text = '''
        The market reality is clear: there is a massive need to create a way for fintech applications to scale globally that allow businesses to invest in expansion, not building infrastructure. Developers need to easily integrate functionality to collect and disburse funds in any local currency, issue cards, extend ewallet functionality, manage KYC and compliance processes, all without having to worry about local regulatory issues. This led Rapyd to launch “Fintech-as-a-Service”, a way to move beyond the era of just integrating payments by providing a full stack of integrated payments, commerce and financial services capabilities that can be embedded into any application.
        We started our journey at Rapyd as a mobile payments company, but soon realized that a much bigger problem existed that needed to be solved. In 2016, we decided to build an e-wallet product that would allow a consumer to withdraw cash from an ATM in any country, without a bank account. We began with just a single country but found it required integration with seven different systems and local services, as well as managing licensing and regulatory requirements, something that simply was not scalable globally. As commerce is becoming increasingly cross-border and at the same time more local, this proved to be a true barrier to innovation.
        Today, Rapyd helps businesses create great local commerce experiences anywhere. We build the technology that removes the back-end complexities of cross-border commerce while providing local payments expertise. Global ecommerce companies, technology firms, marketplaces, and financial institutions use our fintech-as-a-service platforms—Collect, Disburse, Wallet, and Issuing—to seamlessly embed localized fintech and payments capabilities into their applications in a simple way. We have also built the Rapyd Global Payments Network that lets businesses access the world’s largest local payment network with over 900 locally preferred payment methods including, bank transfers, ewallets, cash in more than 100 countries.
        '''
        wc_service = word_cloud_service.WordCloudService()
        img = wc_service.create_wordCloud(text)
        return stream( lambda response : streaming_fn(response,img))
    except Exception as ex:
        print(ex)

async def streaming_fn(response, img):
  
    output = io.BytesIO()
    img.save(output, format="png")
    await response.write(output.getvalue())